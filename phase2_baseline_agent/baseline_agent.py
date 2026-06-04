# Phase 2: Basic Rule-Based Portfolio Copilot

def portfolio_agent(user_input):
    user_input = user_input.lower()

    if "underperform" in user_input:
        return "The portfolio may have underperformed due to sector allocation or market conditions. Detailed analysis requires benchmark comparison."

    elif "allocation" in user_input:
        return "The portfolio allocation should be aligned with the client's risk profile. Please review equity, debt, and cash distribution."

    elif "risk" in user_input:
        return "Concentration risk may arise if a large portion of the portfolio is allocated to a single asset or sector."

    elif "client" in user_input:
        return "For client discussions, focus on performance, risk, and alignment with financial goals."

    elif "rebalance" in user_input:
        return "Rebalancing decisions should be reviewed by the advisor. This system cannot execute transactions."

    else:
        return "I'm unable to provide a detailed answer. Please provide more specific portfolio-related queries."


# Run the agent
print("AI Portfolio Copilot (Baseline Version)")
print("Type 'exit' to stop\n")

while True:
    user_query = input("Ask your question: ")
    
    if user_query.lower() == "exit":
        print("Exiting agent...")
        break
    
    response = portfolio_agent(user_query)
    print("Agent:", response)
    print("-" * 50)