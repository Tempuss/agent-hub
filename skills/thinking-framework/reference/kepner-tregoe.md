# Kepner-Tregoe

## Definition
Systematic approach for problem analysis, decision analysis, cause analysis, and potential problem analysis.

## Steps
1. **Problem Analysis**: What is wrong? Where, when, extent? What changed?
2. **Decision Analysis**: State decision, set criteria (must-have vs. nice-to-have), evaluate alternatives, identify risks
3. **Cause Analysis**: Identify possible causes, test hypotheses, verify true cause
4. **Potential Problem Analysis**: Future problems? Prevention? Contingency plans?

## Pros
- Comprehensive and systematic
- Separates problem-solving from decision-making
- Reduces bias through structured process

## Cons
- Time-consuming for urgent issues
- Can feel bureaucratic
- Requires team buy-in

## Example
**Server Downtime Investigation**:

- **Problem Analysis**: Server down from 2-4pm on Tuesday; only affected production environment
- **Decision Analysis**: Options: restart server, restore from backup, rebuild from scratch; criteria: speed, data safety, cost → Decision: restore from backup
- **Cause Analysis**: Hypotheses tested: DDoS attack (no), bad deployment (yes - new code had memory leak), hardware failure (no) → True cause: untested code deployment
- **Potential Problem Analysis**: Prevent future: implement staging environment, automated testing, gradual rollout; Contingency: keep hourly backups

## When to Use
- Critical decision-making
- Complex problem analysis
- Risk management
- Strategic planning

## Success Context
- **decision_making**: Effective for systematic decisions
- ⚠️ **NOT for creative_innovation** (0% success rate)
- Best for: High-stakes decisions requiring thorough analysis
- Avoid for: Creative problems (too structured/bureaucratic)
