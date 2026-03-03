import streamlit as st
import asyncio
from agents.search_agent import search_agent

st.set_page_config(page_title="AI Search Agent", page_icon="🤖")

st.title("🤖 Pydantic AI Internet Search Agent")
st.write("Ask anything and get the latest information from the web!")

# Input box
user_query = st.text_input("Enter your query:")

# Number of results (optional)
max_results = st.number_input("Max search results", min_value=1, max_value=10, value=5)

if st.button("Search"):
    if user_query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Searching the web..."):
            async def run_agent():
                response = await search_agent.run(user_query)
                return response.output

            result = asyncio.run(run_agent())

            if result:
                for i, r in enumerate(result, start=1):
                    if isinstance(r, dict):
                        title = r.get("title", "No title")
                        href = r.get("href")
                        body = r.get("body")
                    elif isinstance(r, str):
                        title = r
                        href = None
                        body = None
                    else:
                        title = getattr(r, "title", None) or getattr(r, "name", None) or str(r)
                        href = getattr(r, "href", None)
                        body = getattr(r, "body", None)

                    st.markdown(f"**{i}. {title or 'No title'}**")
                    if href:
                        st.markdown(f"[Link]({href})")
                    if body:
                        st.markdown(body)
            else:
                st.info("No results found.")