# Agentic-AI-AI-News-Web-Chatbot

https://agentic-ai-ai-news-web-chatbot-3l84agbtar9dywk28gxnkc.streamlit.app/ 

# Agentic AI Chatbot

A Streamlit-based chatbot powered by LangGraph, LangChain, and LLMs, featuring agentic workflows and integrated search tools.

## Features
- Modular agentic graph architecture using LangGraph
- Multiple use cases selectable via UI
- Integration with LangChain tools (TavilySearch)
- AI-powered news summarization
- Persistent state management
- Modern Streamlit UI

## Use Cases
### 1. Basic Chatbot
Interact with a standard LLM-powered chatbot for general queries and conversation.

### 2. Chatbot with Search Tool
Ask questions that require up-to-date information. The chatbot uses TavilySearch to fetch relevant web results and provides answers with citations.

### 3. AI News Summarizer
Fetches and summarizes the latest global Artificial Intelligence news. Select frequency (daily, weekly, monthly, yearly) to get a markdown summary of recent AI news articles, including date, summary, and source link.

## How to Use
1. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```
2. **Set your API keys:**
	- Add your TAVILY_API_KEY to environment variables or enter it in the UI.
3. **Run the app:**
	```powershell
	streamlit run app.py
	```
4. **Select a use case:**
	- Choose from Basic Chatbot, Chatbot with Search Tool, or AI News Summarizer in the UI.
5. **Start chatting!**

## Project Structure
```
app.py
requirements.txt
src/
  langgraphagenticai/
	 main.py
	 graph/
	 LLMS/
	 Nodes/
	 state/
	 tools/
	 ui/
```

## Configuration
- UI configuration: `src/langgraphagenticai/ui/uiconfigfile.ini`
- State management: `src/langgraphagenticai/state/state.py`
- Node logic: `src/langgraphagenticai/Nodes/`
- Search tool: `src/langgraphagenticai/tools/search_tool.py`

## Credits
- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Uses [LangChain](https://github.com/langchain-ai/langchain) and [langchain-tavily](https://github.com/langchain-ai/langchain-tavily)
- UI by [Streamlit](https://streamlit.io/)

## License
MIT
