from conversational_xagent import ConversationalXAgent

def test_chat():
    agent = ConversationalXAgent()
    result = agent.chat("What is the capital of France?")
    assert "Paris" in result
    print("✅ Test passed:", result)

if __name__ == "__main__":
    test_chat()
