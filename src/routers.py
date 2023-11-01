from llama_index.tools import ToolMetadata
from llama_index.selectors.llm_selectors import LLMSingleSelector
import os
from .triage import fetch_figure,fetch_pages,fetch_sections,fetch_table,retrieve
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
def router(query):
    choices = [
        ToolMetadata(description="Get the text contained in the pages listed", name="fetch_pages"),
        ToolMetadata(description="Get the text contained in the section listed", name="fetch_sections"),
        ToolMetadata(description="Get the text contained in the figure caption listed", name="fetch_figure"),
        ToolMetadata(description="Get the text contained in the table caption listed", name="fetch_table"),
        ToolMetadata(description="Issue a natural language query over the document, and fetch relevant chunks.",
                     name="retrieve"),
    ]

    # choices as a list of strings
    #choices = ["fetch_pages", "fetch_sections", "fetch_figure", "fetch_table", "retrieve"]
    selector = LLMSingleSelector.from_defaults()
    result = selector.select(choices, query=query).selections
    flag = result[0].index
    if flag == 0:
        fetch_pages(query=query)
    elif flag == 1:
        fetch_sections()
    elif flag == 2:
        fetch_figure()
    elif flag == 3:
        fetch_table()
    elif flag == 4:
        retrieve()
    else:
        print("No match found")