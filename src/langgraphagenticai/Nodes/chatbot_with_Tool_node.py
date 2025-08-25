from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """Node for a chatbot with tool capabilities."""
    
    def __init__(self, model):
        self.llm = model

    def process(self, state: State):
        """Process the chatbot interaction with tools."""
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        #simulate tool specific logic
        tools_response = f"Tools integration for: {user_input}"

        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """Return a chatbot node function"""

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic that uses the LLM with tools.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node