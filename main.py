from moya.tools.ephemeral_memory import EphemeralMemory
from core.orchestrator import setup_orchestrator
import time

def generate_technical_question(orchestrator, thread_id, topic):
    prompt = f"Generate a specific technical interview question about {topic}"
    return orchestrator.orchestrate(
        thread_id=thread_id,
        user_message=prompt,
        agent_override="technical_agent"
    )

def generate_behavioral_question(orchestrator, thread_id):
    prompt = "Generate a behavioral interview question about professional skills"
    return orchestrator.orchestrate(
        thread_id=thread_id,
        user_message=prompt,
        agent_override="behavioral_agent"
    )

def analyze_answer(orchestrator, thread_id, question, answer, question_type):
    analysis_prompt = f"""
    Analyze this interview response critically:
    Question: {question}
    Answer: {answer}
    
    Provide:
    1. Accuracy score (0-10)
    2. Specific strengths
    3. Concrete weaknesses
    4. Suggested better answer
    
    Be honest and constructive. If answer is wrong, say so clearly.
    """
    
    agent = "technical_agent" if question_type == "technical" else "behavioral_agent"
    return orchestrator.orchestrate(
        thread_id=thread_id,
        user_message=analysis_prompt,
        agent_override=agent
    )

def conduct_interview(orchestrator, thread_id):
    # Get interview topic from user
    print("\nPlease select topic for interview (e.g., Python, Java, System Design, etc.):")
    topic = input("Your interview topic: ").strip()
    
    EphemeralMemory.store_message(
        thread_id=thread_id, 
        sender="system", 
        content=f"Interview started on topic: {topic}"
    )
    
    # Technical questions phase
    print(f"\n=== Technical Questions on {topic} ===")
    technical_qa = []
    for i in range(1, 4):
        question = generate_technical_question(orchestrator, thread_id, topic)
        print(f"\nQuestion {i}: {question}")
        
        answer = input("Your answer: ").strip()
        analysis = analyze_answer(orchestrator, thread_id, question, answer, "technical")
        technical_qa.append((question, answer, analysis))
        print(f"\nDetailed Analysis:\n{analysis}")

    # Behavioral questions phase
    print("\n=== Behavioral Questions ===")
    behavioral_qa = []
    for i in range(1, 4):
        question = generate_behavioral_question(orchestrator, thread_id)
        print(f"\nQuestion {i}: {question}")
        
        answer = input("Your answer: ").strip()
        analysis = analyze_answer(orchestrator, thread_id, question, answer, "behavioral")
        behavioral_qa.append((question, answer, analysis))
        print(f"\nDetailed Analysis:\n{analysis}")
    
    # Final evaluation
    print("\n=== Final Evaluation ===")
    evaluation_prompt = f"""
    Conduct a rigorous final evaluation based on:
    
    TECHNICAL PERFORMANCE:
    {technical_qa}
    
    BEHAVIORAL PERFORMANCE:
    {behavioral_qa}
    
    Provide:
    1. Overall score (0-100) with breakdown
    2. 3 key strengths
    3. 3 critical weaknesses
    4. Clear hiring recommendation (Strong Yes/Yes/No/Strong No)
    5. Specific improvement plan
    
    Be brutally honest - this is a real hiring decision.
    """
    
    final_evaluation = orchestrator.orchestrate(
        thread_id=thread_id,
        user_message=evaluation_prompt,
        agent_override="feedback_agent"
    )
    print(f"\nCOMPREHENSIVE EVALUATION:\n{final_evaluation}")

def main():
    orchestrator = setup_orchestrator()
    thread_id = f"interview_{int(time.time())}"
    
    print("\n" + "="*50)
    print("INTERVIEW PREPARATION ASSISTANT".center(50))
    print("="*50)
    print("\nThis session will include:")
    print("- 3 Technical questions on your chosen topic")
    print("- 3 Behavioral questions")
    print("- Detailed feedback after each answer")
    print("- Final comprehensive evaluation")
    print("\nType 'exit' at any time to end the session\n")
    
    conduct_interview(orchestrator, thread_id)
    
    EphemeralMemory.store_message(
        thread_id=thread_id,
        sender="system",
        content="Interview session completed"
    )

if __name__ == "__main__":
    main()