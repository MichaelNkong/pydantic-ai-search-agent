from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

from tools.search_internet import search_internet
from dotenv import load_dotenv
load_dotenv()
model = OpenAIChatModel("gpt-4o-mini")

search_agent = Agent(
    model=model,
    tools=[search_internet],
    system_prompt=(
        "You are a research assistant. "
        "Use the search_internet tool whenever the user asks about "
        "current events, news, or recent information."
    ),
)