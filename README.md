# Capstone Project Phase 8 and Phase 9 Add-on

This package completes the missing deployment-readiness and evaluation requirements for the AI Portfolio Copilot capstone project.

## Add these folders to the final capstone submission

```text
phase8_deployment/
phase9_evaluation/
```

## Phase 8 Covers
- Local CLI deployment
- Local Streamlit app deployment
- Runtime logging
- Latency capture
- Graceful error handling
- PII-safe log redaction
- Finance-domain safety refusal
- Deployment instructions and limitations

## Phase 9 Covers
- Repeatable evaluation harness
- Evaluation test cases
- Safety tests
- Failure analysis
- Before/after improvement evidence
- Governance and ethics review
- Evaluation report

## How to Run

### Run CLI
```bash
cd phase8_deployment
python cli.py
```

### Run Streamlit App
```bash
cd phase8_deployment
pip install -r requirements.txt
streamlit run app.py
```

### Run Evaluation
```bash
cd phase9_evaluation
python evaluation_harness.py
```

## Final Submission Note
The earlier submission covered Phase 1 to Phase 7. This add-on completes Phase 8 and Phase 9, addressing deployment readiness, logging, latency, error handling, evaluation, safety testing, failure analysis, before/after fixes, and governance for a finance decision-support agent.

## Final Project Completion

The project was extended through Phase 8 and Phase 9 to satisfy deployment-readiness and evaluation-review requirements.

### Phase 8 Additions
- Streamlit deployment wrapper
- Runtime logging
- Latency monitoring
- Graceful error handling
- PII redaction
- Safety refusal enforcement

### Phase 9 Additions
- Evaluation harness
- Failure analysis
- Governance review
- Safety testing
- Before/after improvement analysis

## Security Note

API keys are handled securely using environment variables and are excluded from submission artifacts.
