# Governance, Ethics, and Finance Safety Review

## Domain Context
The AI Portfolio Copilot operates in a finance-related workflow. Therefore, the system must be treated as a decision-support assistant, not as an autonomous financial advisor or transaction executor.

## Safety Principles
1. No personalized financial advice without complete suitability assessment.
2. No guaranteed return language.
3. No direct buy/sell recommendations.
4. No execution of financial transactions.
5. Escalation to a licensed advisor or human analyst for high-risk or ambiguous cases.
6. PII-safe logging and audit trail design.
7. Clear communication of uncertainty when documents or data are missing.

## Human-in-the-Loop Requirement
The agent may assist with analysis, summarization, risk identification, and draft communication. Final recommendations, suitability decisions, and client-facing advice must be reviewed by a qualified human professional.

## Audit and Logging
Logs should support debugging and governance review but must not store sensitive personal data. Phase 8 implements redaction of obvious PII before writing logs.

## Known Limitations
- Pattern-based safeguards are useful but not perfect.
- Enterprise deployment requires authentication, access control, encryption, monitoring, and compliance review.
- The agent should not be treated as a SEBI-registered advisor or legal/tax authority.

## Improvement Roadmap
- Add stronger policy classifier for unsafe requests.
- Add role-based access control.
- Add encrypted document storage.
- Add retrieval citation enforcement.
- Add reviewer approval workflow before client-facing communication.
- Add monitoring dashboard for safety refusals, latency, and error rates.

## Financial Safety Governance

The AI Portfolio Copilot was designed as a decision-support system only.

The system explicitly refuses:
- guaranteed return requests
- direct transactional execution
- personalized financial advice
- suitability-sensitive recommendations without investor context

The deployment wrapper includes:
- runtime logging
- PII redaction
- refusal-safe handling
- escalation to licensed advisors
- audit-safe observability

This aligns with banking and financial AI safety expectations.