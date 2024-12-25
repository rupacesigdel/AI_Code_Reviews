class LangGraphAgent:
    def __init__(self, name, description, graph):
        self.name = name
        self.description = description
        self.graph = graph

    def execute(self, user_code):
        result = f"Agent {self.name} is analyzing the code: {user_code}"
        return result
