from agent_core import generate_response


def main():
    print("AI Portfolio Copilot CLI - Phase 8 Deployment Wrapper")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Session ended.")
            break
        result = generate_response(user_input)
        print(f"Agent [{result['status']} | {result['latency_ms']} ms]:")
        print(result["response"])
        print("-" * 80)


if __name__ == "__main__":
    main()
