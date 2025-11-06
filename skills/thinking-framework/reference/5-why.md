# 5 Why Technique

## Definition
Repeatedly ask "Why?" (at least 5 times) to find the root cause of a problem.

## Steps
1. Define the problem clearly
2. Ask "Why did this happen?" (Why 1)
3. For the answer, ask "Why?" again (Why 2)
4. Continue for Why 3, Why 4, Why 5
5. Identify the fundamental root cause

## Pros
- Simple and quick to apply
- No special tools required
- Gets to root cause efficiently

## Cons
- Quality depends on question framing
- Can oversimplify complex problems with multiple causes
- Requires domain knowledge to ask right questions

## Example
**Problem**: Server crashed

- **Why 1**: Why did the server crash? → Memory exhausted
- **Why 2**: Why was memory exhausted? → Memory leak in application
- **Why 3**: Why was there a memory leak? → Objects not properly garbage collected
- **Why 4**: Why weren't objects collected? → Missing cleanup in connection pooling
- **Why 5**: Why was cleanup missing? → Testing stage didn't include load testing

**Root Cause**: Insufficient testing methodology (load testing omitted)

## When to Use
- Root cause analysis
- Problem investigation
- Quality improvement initiatives
- Post-mortem analysis

## Success Context
- **root_cause_analysis**: 100% success rate
- Best for: Single chain of causation
- Avoid for: Multi-causal complex systems (use Fishbone instead)
