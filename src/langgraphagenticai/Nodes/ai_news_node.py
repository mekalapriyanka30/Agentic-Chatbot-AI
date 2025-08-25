from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        """
        Initializes the AI News Node with TavilySearch and GROQ LLM.
        """
        self.tavily = TavilySearch()
        self.llm = llm
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetches the latest AI news based on the specified time frame.

        Args:
            state (dict): The input state containing parameters like time_frame.

        Returns:
            dict: A dictionary containing the fetched news articles.
        """
        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'day', 'weekly': 'week',
                          'monthly': 'month', 'year': 'year'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.invoke({
            "query": "Top Artificial Intelligence (AI) technology news Globally",
            "topic": "news",
            "time_range": time_range_map[frequency],
            "include_answer": "advanced",
            "max_results": 20,
            "days": days_map[frequency],
        })

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state

    def summarize_news(self, state: dict) -> dict:
        """
        Summarizes the fetched news articles using the LLM.

        Args:
            state (dict): The input state containing 'news_data'.
        Returns:
            dict: Updated state with 'summary' key containing the summarised news.
        """

        news_items = self.state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date (latest first)
            - Source URL as link

            Use format:
            ### [Date]

            - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items

        ])

        response = self.llm.invoke(
            prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state

    def save_result(self, state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AI_News/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        return self.state
