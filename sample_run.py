from xagent_adapter import XAgentAdapter

if __name__ == "__main__":
    agent = XAgentAdapter()
    print("🤖 XAgent Integration Test")
    query = "What is the capital of France?"
    response = agent.run(query)
    print("User:", query)
    print("Agent:", response)
