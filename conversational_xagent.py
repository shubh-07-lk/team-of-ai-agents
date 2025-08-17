from xagent_adapter import XAgentAdapter

class ConversationalXAgent:
    def __init__(self):
        self.agent = XAgentAdapter()

    def chat(self, query: str):
        return self.agent.run(query)
