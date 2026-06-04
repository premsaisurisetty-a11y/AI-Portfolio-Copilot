# Phase 9 Evaluation Report

## Objective
Phase 9 evaluates the AI Portfolio Copilot for quality, consistency, safety, and engineering readiness.

## Evaluation Method
A repeatable evaluation harness was created using `evaluation_harness.py` and `evaluation_test_cases.csv`. The harness runs predefined test cases, captures latency, response status, preview text, and safety-related scoring.

## Metrics Used
| Metric | Description |
|---|---|
| Safety OK | Whether unsafe finance requests are refused |
| Caveat OK | Whether decision-support and non-advice caveats are included |
| Escalation OK | Whether human/licensed advisor escalation is mentioned |
| Uncertainty OK | Whether missing information is acknowledged |
| Latency | Runtime captured in milliseconds |

## Test Categories
- Normal finance analysis
- Missing information
- Unsafe guaranteed-return request
- Transaction request
- PII handling
- Retrieval gap
- Tool usage
- Memory/context handling

## Expected Outcome
The agent should provide useful decision-support analysis while refusing unsafe requests, avoiding hallucination, redacting PII in logs, and escalating high-risk cases.

## Root Cause and Fix
At least one failure case was analyzed: direct investment advice and guaranteed-return requests. The fix added pattern-based safety refusal, suitability caveats, and escalation language.

## Conclusion
The project now includes a structured evaluation approach, safety testing, root cause analysis, before/after evidence, and governance review. This completes the Phase 9 engineering review requirement.

## Deployment Evaluation Evidence

The deployment wrapper was tested using multiple finance-domain safety scenarios.

### Tested Scenarios
1. Guaranteed return request
2. Direct transaction execution request
3. Missing suitability information
4. PII redaction validation

### Key Observations
- Unsafe financial requests were refused safely.
- Direct money movement instructions were blocked.
- Runtime latency was captured successfully.
- Logs demonstrated audit-safe observability.
- PII information was redacted from logs.

### Evidence Files
- phase8_safe_refusal_guaranteed_returns.png
- phase8_transaction_refusal.png
- phase8_runtime_logs.png
