import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "session_memory.json"
MODEL_NAME = "gpt-3.5-turbo"

# -----------------------------
# Memory helpers
# -----------------------------
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "client_name": None,
        "risk_profile": None,
        "investment_horizon": None,
        "goal": None,
        "conversation_history": []
    }

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def reset_memory():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)

# -----------------------------
# Planning logic
# -----------------------------
def create_plan(user_query, memory):
    plan = []

    if memory["risk_profile"] or memory["goal"] or memory["investment_horizon"]:
        plan.append("Use stored client profile context")

    if "suitable" in user_query.lower() or "allocation" in user_query.lower():
        plan.append("Check alignment between allocation and risk profile")

    if "discuss" in user_query.lower() or "review" in user_query.lower():
        plan.append("Summarize key talking points for advisor meeting")

    if not plan:
        plan.append("Provide professional portfolio advisory response")

    return plan

# -----------------------------
# Update memory from user input
# -----------------------------
def update_memory_from_input(user_query, memory):
    lower_q = user_query.lower()

    if "moderate" in lower_q:
        memory["risk_profile"] = "Moderate"
    elif "conservative" in lower_q:
        memory["risk_profile"] = "Conservative"
    elif "aggressive" in lower_q:
        memory["risk_profile"] = "Aggressive"

    if "10 years" in lower_q:
        memory["investment_horizon"] = "10 years"
    elif "5 years" in lower_q:
        memory["investment_horizon"] = "5 years"

    if "wealth creation" in lower_q:
        memory["goal"] = "Wealth creation"
    elif "retirement" in lower_q:
        memory["goal"] = "Retirement"

    memory["conversation_history"].append(user_query)

# -----------------------------
# Generate answer with memory
# -----------------------------
def answer_with_memory(user_query, memory):
    plan = create_plan(user_query, memory)

    system_prompt = f"""
You are an AI Portfolio Copilot for a wealth manager.

Stored Client Context:
- Risk Profile: {memory.get('risk_profile')}
- Investment Horizon: {memory.get('investment_horizon')}
- Goal: {memory.get('goal')}

Planning Steps:
{chr(10).join(['- ' + step for step in plan])}

Instructions:
1. Use stored memory if relevant.
2. Answer clearly and professionally.
3. Do not fabricate facts.
4. If context is missing, say so.
5. This is decision support only.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        temperature=0.3
    )

    return plan, response.choices[0].message.content

# -----------------------------
# Generate answer without memory
# -----------------------------
def answer_without_memory(user_query):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Portfolio Copilot. "
                    "Answer professionally, but do not use any stored context."
                )
            },
            {"role": "user", "content": user_query}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

# -----------------------------
# Main multi-turn demo
# -----------------------------
def main():
    print("Phase 6 - Portfolio Copilot with Planning, Memory & Context")
    print("=" * 70)

    memory = load_memory()

    test_inputs = [
        "The client has a moderate risk profile, a 10 years horizon, and a wealth creation goal.",
        "Is this portfolio suitable for the client?",
        "What should I discuss with the client in the next review meeting?"
    ]

    for user_query in test_inputs:
        print(f"\nUSER: {user_query}")
        update_memory_from_input(user_query, memory)

        print("\nWITHOUT MEMORY:")
        print(answer_without_memory(user_query))

        print("\nWITH MEMORY + PLANNING:")
        plan, answer = answer_with_memory(user_query, memory)

        print("\nPlan Used:")
        for step in plan:
            print("-", step)

        print("\nAnswer:")
        print(answer)
        print("\n" + "-" * 70)

    save_memory(memory)

    print("\nCurrent Stored Memory:")
    print(json.dumps(memory, indent=2))

    print("\nMemory retention rule:")
    print("- Session memory is retained in session_memory.json")
    print("- Use reset_memory() to clear old client context before a new client session")

if __name__ == "__main__":
    main()