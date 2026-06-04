import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPTS = {
    "v1_basic": """
You are an AI Portfolio Copilot for a wealth manager.
Answer the user's portfolio-related question clearly and professionally.
""",
    "v2_structured": """
You are an AI Portfolio Copilot for a wealth manager.
Answer clearly, professionally, and in a structured way.

Rules:
1. Focus only on portfolio decision support.
2. Do not suggest executing trades or transactions.
3. If information is missing, say so clearly.
4. Keep the answer concise and practical.
""",
    "v3_safety_first": """
You are an AI Portfolio Copilot for a wealth manager.

Your role:
- Support portfolio review and advisory preparation
- Provide decision support only
- Do not execute transactions or give guaranteed return statements

Instructions:
1. Answer in 4 parts:
   - Summary
   - Key Reason
   - Risk / Caution
   - Advisor Next Step
2. If data is insufficient, explicitly mention uncertainty.
3. Do not fabricate portfolio facts.
4. Escalate complex or high-risk situations to a human advisor.
5. Keep tone professional and client-safe.
"""
}

TEST_QUESTIONS = [
    "Why did my portfolio underperform this quarter?",
    "Is my current allocation suitable for a moderate-risk client?",
    "What should I discuss with the client in the next review meeting?"
]

def get_response(prompt_key, user_query):
    system_prompt = PROMPTS[prompt_key]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

def main():
    print("Phase 3 - AI Portfolio Copilot (LLM Version)")
    print("=" * 60)

    for prompt_name in PROMPTS:
        print(f"\n--- Testing Prompt: {prompt_name} ---\n")
        for q in TEST_QUESTIONS:
            print(f"Question: {q}")
            try:
                answer = get_response(prompt_name, q)
                print("Answer:")
                print(answer)
            except Exception as e:
                print("Error:", str(e))
            print("-" * 60)

if __name__ == "__main__":
    main()