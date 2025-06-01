from moya.tools.ephemeral_memory import EphemeralMemory
from core.orchestrator import setup_orchestrator


def main():
    orchestrator = setup_orchestrator()
    thread_id = "interview_thread"

    print("Interview Prep Chatbot (type 'exit' to quit)\n")

    EphemeralMemory.store_message(thread_id=thread_id, sender="system", content=f"Session started: {thread_id}")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        EphemeralMemory.store_message(thread_id=thread_id, sender="user", content=user_input)

        session_summary = EphemeralMemory.get_thread_summary(thread_id)
        enriched_message = f"{session_summary}\nUser message: {user_input}"

        print("Assistant: ", end="", flush=True)

        response = orchestrator.orchestrate(thread_id=thread_id, user_message=enriched_message)
        print(response)

        EphemeralMemory.store_message(thread_id=thread_id, sender="assistant", content=response)


if __name__ == "__main__":
    main()
