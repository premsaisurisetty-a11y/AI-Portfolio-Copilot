# Phase 8: Deployment Readiness Instructions

## Objective
This phase converts the AI Portfolio Copilot from a prototype into a reproducible local deployment with logging, latency capture, error handling, and safety-aware responses.

## Local CLI Deployment
1. Open terminal in the `phase8_deployment` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the CLI:
   ```bash
   python cli.py
   ```
4. Enter sample finance workflow questions and review responses.

## Local Streamlit Deployment
1. Open terminal in the `phase8_deployment` folder.
2. Run:
   ```bash
   streamlit run app.py
   ```
3. Open the local URL shown by Streamlit.

## Logging and Tracing
Runtime logs are written to:

```text
phase8_deployment/logs/agent_runtime.log
```

The logger captures:
- timestamp
- request status
- latency in milliseconds
- safe error messages
- PII-redacted request text

## Graceful Failure Handling
The agent handles:
- empty input
- unsafe/high-risk financial requests
- runtime exceptions
- user requests that require escalation

## Security Assumptions
- API keys must not be hard-coded.
- Sensitive personal data must not be stored in logs.
- Logs should redact phone numbers, emails, account-like numbers, and Aadhaar-like numbers.

## Deployment Limitations
- This deployment is local-first.
- The app demonstrates production-readiness patterns, but a full enterprise deployment would require authentication, role-based access, encrypted storage, monitoring dashboards, and compliance approval.
