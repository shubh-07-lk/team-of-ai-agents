from xagent_adapter import XAgentAdapter

class DialogueAgentWithToolsXAgent:
    def __init__(self, tools=None):
        self.agent = XAgentAdapter()
        self.tools = tools or []

    def run(self, query: str):
        # Tools logic can be added here
        return self.agent.run(query)
