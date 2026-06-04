import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = "gpt-3.5-turbo"
FEEDBACK_FILE = "feedback_memory.json"

# -----------------------------
# Feedback storage helpers
# -----------------------------
# -----------------------------
# Feedback storage helpers
# -----------------------------
def load_feedback():
    default_feedback = {
        "response_style": "standard",
        "include_caution": False,
        "format": "paragraph"
    }

    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return default_feedback
                return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return default_feedback

    return default_feedback


def save_feedback(feedback):
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(feedback, f, indent=2)
# -----------------------------
# Update feedback preferences
# -----------------------------
def apply_feedback_signal(user_feedback, feedback_memory):
    lower_f = user_feedback.lower()

    if "concise" in lower_f or "short" in lower_f:
        feedback_memory["response_style"] = "concise"

    if "structured" in lower_f or "bullet" in lower_f or "points" in lower_f:
        feedback_memory["format"] = "bullet"

    if "caution" in lower_f or "risk" in lower_f or "careful" in lower_f:
        feedback_memory["include_caution"] = True

    return feedback_memory

# -----------------------------
# Base answer (before adaptation)
# -----------------------------
def answer_before_adaptation(query):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Portfolio Copilot for a wealth manager. "
                    "Answer professionally."
                )
            },
            {"role": "user", "content": query}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# -----------------------------
# Adapted answer (after feedback)
# -----------------------------
def answer_after_adaptation(query, feedback_memory):
    style = feedback_memory["response_style"]
    fmt = feedback_memory["format"]
    caution = feedback_memory["include_caution"]

    system_prompt = f"""
You are an AI Portfolio Copilot for a wealth manager.

Adaptive Feedback Preferences:
- Response Style: {style}
- Format: {fmt}
- Include Caution: {caution}

Instructions:
1. Adjust the answer based on the feedback preferences.
2. If format is bullet, use clear bullet points.
3. If response style is concise, keep the answer short and sharp.
4. If include caution is true, add a risk/caution note where relevant.
5. This is decision support only.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# -----------------------------
# Main
# -----------------------------
def main():
    print("Phase 7 - Adaptive Behaviour")
    print("=" * 70)

    query = "What should I discuss with the client in the next review meeting?"
    user_feedback = "Please make the answer more concise, structured in bullet points, and include caution where needed."

    feedback_memory = load_feedback()

    print("TEST QUERY:")
    print(query)
    print("\nUSER FEEDBACK SIGNAL:")
    print(user_feedback)

    print("\nBEFORE ADAPTATION:")
    before_answer = answer_before_adaptation(query)
    print(before_answer)

    feedback_memory = apply_feedback_signal(user_feedback, feedback_memory)
    save_feedback(feedback_memory)

    print("\nUPDATED FEEDBACK MEMORY:")
    print(json.dumps(feedback_memory, indent=2))

    print("\nAFTER ADAPTATION:")
    after_answer = answer_after_adaptation(query, feedback_memory)
    print(after_answer)

    print("\n" + "=" * 70)
    print("Adaptive behavior note:")
    print("- Feedback is stored in feedback_memory.json")
    print("- Future responses use the updated preferences")
    print("- This simulates learning from user feedback")

if __name__ == "__main__":
    main()