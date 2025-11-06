#!/usr/bin/env python3
"""
Skill Auto-Activator
자동 스킬 감지 및 활성화 시스템

Usage as Hook:
  - Place in .claude/hooks/user-prompt-submit.py
  - Or import and use: from skill_auto_activator import SkillActivator
"""

import os
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class SkillActivator:
    """키워드 기반 스킬 자동 활성화 시스템"""

    def __init__(self, index_path: Optional[str] = None):
        """
        Initialize SkillActivator

        Args:
            index_path: Path to INDEX.yaml (optional, auto-detect if None)
        """
        if index_path is None:
            # Auto-detect INDEX.yaml from script location
            script_dir = Path(__file__).parent.parent
            index_path = script_dir / "INDEX.yaml"

        self.index_path = Path(index_path)
        self.config = self._load_config()
        self.skills = self.config.get("skills", {})
        self.activation_config = self.config.get("activation_config", {})
        self.keyword_weights = self.config.get("keyword_weights", {})

    def _load_config(self) -> Dict:
        """Load INDEX.yaml configuration"""
        try:
            with open(self.index_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"❌ INDEX.yaml not found at: {self.index_path}", file=sys.stderr)
            return {}
        except yaml.YAMLError as e:
            print(f"❌ Error parsing INDEX.yaml: {e}", file=sys.stderr)
            return {}

    def _extract_keywords(self, text: str) -> List[str]:
        """
        Extract keywords from user message

        Args:
            text: User input text

        Returns:
            List of keywords (lowercase, normalized)
        """
        # Korean/English stopwords to filter out
        stopwords = {
            # Korean
            '해줘', '좀', '이거', '저거', '그거', '뭐', '뭔가', '어떻게', '왜', '언제',
            '어디', '누구', '무엇', '어떤', '있어', '없어', '하는', '되는', '같은',
            '있는', '없는', '해서', '해요', '합니다', '이다', '입니다', '새로운',
            '하려고', '있는데', '싶어', '만들어줘', '짜줘', '너무', '복잡한',
            '복잡해서', '찾고',
            # English
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
            'could', 'can', 'may', 'might', 'must', 'shall', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
            'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'what', 'which',
            'who', 'when', 'where', 'why', 'how', 'please', 'just', 'some'
        }

        # Korean particles (조사) to remove
        korean_particles = ['가', '이', '은', '는', '을', '를', '에', '에서', '에게', '께서',
                          '으로', '로', '의', '도', '만', '부터', '까지', '와', '과']

        # Normalize text: lowercase, remove special chars except Korean/English/numbers
        normalized = re.sub(r'[^\w\sㄱ-ㅎㅏ-ㅣ가-힣]', ' ', text.lower())

        # Split into words
        words = []
        for w in normalized.split():
            w = w.strip()
            if len(w) < 2:
                continue

            # Remove Korean particles from end of word
            word_clean = w
            for particle in korean_particles:
                if w.endswith(particle) and len(w) > len(particle) + 1:
                    word_clean = w[:-len(particle)]
                    break

            # Filter stopwords and keep meaningful words
            if word_clean and word_clean not in stopwords:
                words.append(word_clean)

        return words

    def _calculate_match_score(self, user_keywords: List[str], skill_data: Dict) -> float:
        """
        Calculate keyword matching score for a skill

        Args:
            user_keywords: Keywords from user message
            skill_data: Skill metadata from INDEX.yaml

        Returns:
            Match score (0.0 to 1.0+)
        """
        score = 0.0
        max_possible_score = 0.0

        # Get skill keywords (Korean + English)
        skill_keywords_ko = skill_data.get("keywords", {}).get("korean", [])
        skill_keywords_en = skill_data.get("keywords", {}).get("english", [])
        skill_keywords = [k.lower() for k in skill_keywords_ko + skill_keywords_en]

        # Get skill tags and use cases
        skill_tags = [t.lower() for t in skill_data.get("tags", [])]
        skill_use_cases = [u.lower() for u in skill_data.get("use_cases", [])]

        # Calculate max possible score
        max_possible_score = len(user_keywords) * self.keyword_weights.get("exact_match", 2.0)

        if max_possible_score == 0:
            return 0.0

        # Check for compound word matches first (multiple user keywords in one skill keyword)
        matched_user_keywords = set()
        for skill_kw in skill_keywords:
            # Find all user keywords that are substrings of this skill keyword
            matching_parts = [uk for uk in user_keywords if uk in skill_kw and len(uk) >= 2]

            # If 2+ user keywords match this skill keyword, it's a compound match
            if len(matching_parts) >= 2:
                # Mark these keywords as matched
                for uk in matching_parts:
                    matched_user_keywords.add(uk)
                # Give compound match score (higher than partial, lower than exact)
                score += len(matching_parts) * self.keyword_weights.get("compound_match", 1.8)

        # Match remaining keywords individually
        for user_kw in user_keywords:
            if user_kw in matched_user_keywords:
                continue  # Already scored as compound match

            # Exact match
            if user_kw in skill_keywords:
                score += self.keyword_weights.get("exact_match", 2.0)
            # Partial match (substring)
            elif any(user_kw in sk or sk in user_kw for sk in skill_keywords):
                score += self.keyword_weights.get("partial_match", 1.0)
            # Tag match
            elif user_kw in skill_tags:
                score += self.keyword_weights.get("tag_match", 0.5)
            # Use case match
            elif any(user_kw in uc or uc in user_kw for uc in skill_use_cases):
                score += self.keyword_weights.get("use_case_match", 1.5)

        # Normalize to 0-1 range and apply priority multiplier
        normalized_score = score / max_possible_score

        priority = skill_data.get("priority", "medium")
        priority_multipliers = self.activation_config.get("priority_multipliers", {
            "high": 1.5,
            "medium": 1.0,
            "low": 0.7
        })
        multiplier = priority_multipliers.get(priority, 1.0)

        final_score = normalized_score * multiplier

        return min(final_score, 1.0)  # Cap at 1.0

    def detect_skills(self, user_message: str) -> List[Tuple[str, float, Dict]]:
        """
        Detect relevant skills from user message

        Args:
            user_message: User input text

        Returns:
            List of (skill_name, confidence_score, skill_data) sorted by score
        """
        user_keywords = self._extract_keywords(user_message)

        if not user_keywords:
            return []

        matches = []
        global_threshold = self.activation_config.get("confidence_threshold", 0.7)

        for skill_name, skill_data in self.skills.items():
            # Skip if auto_activate is False
            if not skill_data.get("auto_activate", True):
                continue

            score = self._calculate_match_score(user_keywords, skill_data)

            # Use skill-specific threshold if available, otherwise global
            threshold = skill_data.get("confidence_threshold", global_threshold)

            if score >= threshold:
                matches.append((skill_name, score, skill_data))

        # Sort by score (descending)
        matches.sort(key=lambda x: x[1], reverse=True)

        # Limit to max_suggestions
        max_suggestions = self.activation_config.get("max_suggestions", 3)
        return matches[:max_suggestions]

    def format_suggestion(self, matches: List[Tuple[str, float, Dict]]) -> str:
        """
        Format skill suggestions for display

        Args:
            matches: List of (skill_name, confidence_score, skill_data)

        Returns:
            Formatted suggestion text
        """
        if not matches:
            return ""

        mode = self.activation_config.get("mode", "suggest")

        if mode == "auto":
            # Auto mode: return first match
            skill_name, score, skill_data = matches[0]
            description = skill_data.get("description", "")
            return f"""
🔄 **스킬 자동 활성화**
  - 스킬: {skill_name}
  - 신뢰도: {score:.0%}
  - 설명: {description}
"""
        else:
            # Suggest mode: show all matches
            lines = ["", "🎯 **관련 스킬 추천:**", ""]

            for i, (skill_name, score, skill_data) in enumerate(matches, 1):
                description = skill_data.get("description", "")
                lines.append(f"{i}. **{skill_name}** (신뢰도: {score:.0%})")
                lines.append(f"   {description}")
                lines.append("")

            lines.append("💡 스킬을 사용하려면: `/skill [skill-name]` 또는 `@skills/[skill-name]`")

            return "\n".join(lines)

    def process_message(self, user_message: str) -> Optional[str]:
        """
        Process user message and return skill suggestion

        Args:
            user_message: User input text

        Returns:
            Suggestion text or None if no matches
        """
        matches = self.detect_skills(user_message)

        if not matches:
            return None

        return self.format_suggestion(matches)


def main():
    """Main entry point for testing"""
    if len(sys.argv) < 2:
        print("Usage: python skill-auto-activator.py <user_message>")
        print("\nExample:")
        print('  python skill-auto-activator.py "ROI 분석 좀 해줘"')
        sys.exit(1)

    user_message = " ".join(sys.argv[1:])

    activator = SkillActivator()
    suggestion = activator.process_message(user_message)

    if suggestion:
        print(suggestion)
    else:
        print("🔍 관련 스킬을 찾지 못했습니다.")


# Hook integration for Claude Code
def user_prompt_submit_hook(user_message: str) -> str:
    """
    Hook function for Claude Code user-prompt-submit event

    Args:
        user_message: User input text

    Returns:
        Modified message with skill suggestions
    """
    try:
        activator = SkillActivator()
        suggestion = activator.process_message(user_message)

        if suggestion:
            # Prepend suggestion to user message
            return f"{suggestion}\n\n---\n\n{user_message}"
        else:
            return user_message

    except Exception as e:
        # Fail silently, return original message
        print(f"⚠️ Skill auto-activator error: {e}", file=sys.stderr)
        return user_message


if __name__ == "__main__":
    main()
