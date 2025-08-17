class XAgentAdapter:
    def __init__(self):
        # init XAgent here
        pass

    def run(self, query: str) -> str:
        # placeholder response for demo
        if "capital of France" in query:
            return "The capital of France is Paris."
        return "This is a sample response from XAgentAdapter."
