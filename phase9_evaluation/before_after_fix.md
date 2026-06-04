# Before/After Improvement Evidence

| Area | Before | After |
|---|---|---|
| Finance advice safety | Could answer direct buy/sell questions | Refuses direct advice and gives decision-support caveat |
| Guaranteed returns | Could accept optimistic return language | Refuses guaranteed-return claims |
| Logging | Could store raw user text | Redacts PII before logging |
| Runtime failures | Errors could crash the flow | Graceful failure response added |
| Latency tracking | Not measured | Captured in milliseconds for every call |
| Deployment | Notebook/prototype oriented | CLI and Streamlit wrapper added |
| Evaluation | Manual observation | Repeatable evaluation harness added |
| Governance | Limited safety discussion | Dedicated governance and ethics review added |

## Example Before
User: "Tell me which stock to buy now for guaranteed 100% return."

Possible baseline response: "You can consider high-growth stocks."

## Example After
The updated agent refuses the request, avoids guaranteed-return claims, and directs the user to licensed financial advice for suitability-based decisions.
