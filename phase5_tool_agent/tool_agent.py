import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# TOOL 1: Asset Allocation Checker
# -----------------------------
def check_asset_allocation(equity, debt, cash, risk_profile):
    total = equity + debt + cash

    if total != 100:
        return "Allocation must sum to 100%."

    if risk_profile == "Moderate":
        if 60 <= equity <= 70 and 20 <= debt <= 30:
            return "Allocation is suitable for a moderate-risk profile."
        else:
            return "Allocation may not align well with a moderate-risk profile."

    return "Risk profile not recognized."

# -----------------------------
# TOOL 2: Risk Concentration Checker
# -----------------------------
def check_concentration(sector_exposure):
    high_risk_sectors = []

    for sector, value in sector_exposure.items():
        if value > 30:
            high_risk_sectors.append(sector)

    if high_risk_sectors:
        return f"High concentration risk in: {', '.join(high_risk_sectors)}"
    else:
        return "Sector concentration is within acceptable limits."

# -----------------------------
# LLM Response (Without Tools)
# -----------------------------
def answer_without_tools(query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial advisor assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

# -----------------------------
# LLM + Tools Logic
# -----------------------------
def answer_with_tools(query):
    # Example hardcoded portfolio (for demo)
    equity = 70
    debt = 20
    cash = 10
    risk_profile = "Moderate"

    sector_exposure = {
        "Technology": 40,
        "Financials": 25,
        "Healthcare": 15,
        "Energy": 10,
        "Others": 10
    }

    if "allocation" in query.lower():
        return check_asset_allocation(equity, debt, cash, risk_profile)

    elif "risk" in query.lower() or "concentration" in query.lower():
        return check_concentration(sector_exposure)

    else:
        return answer_without_tools(query)

# -----------------------------
# Main
# -----------------------------
def main():
    questions = [
        "Is this portfolio allocation suitable?",
        "Is there any sector concentration risk?",
        "What should I discuss with the client?"
    ]

    print("Phase 5 - Portfolio Copilot with Tools")
    print("=" * 60)

    for q in questions:
        print(f"\nQUESTION: {q}")

        print("\nWITHOUT TOOLS:")
        print(answer_without_tools(q))

        print("\nWITH TOOLS:")
        print(answer_with_tools(q))

        print("\n" + "-" * 60)

if __name__ == "__main__":
    main()