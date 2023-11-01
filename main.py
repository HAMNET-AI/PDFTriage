from llama_index.tools import ToolMetadata
from llama_index.selectors.llm_selectors import LLMSingleSelector
import os
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["OPENAI_API_KEY"] = "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"
if __name__ == '__main__':
    # choices as a list of tool metadata
    choices = [
        ToolMetadata(description="Get the text contained in the pages listed", name="fetch_pages"),
        ToolMetadata(description="Get the text contained in the section listed", name="fetch_sections"),
        ToolMetadata(description="Get the text contained in the figure caption listed", name="fetch_figure"),
        ToolMetadata(description="Get the text contained in the table caption listed", name="fetch_table"),
        ToolMetadata(description="Issue a natural language query over the document, and fetch relevant chunks.", name="retrieve"),
    ]

    # choices as a list of strings
    choices = ["fetch_pages", "fetch_sections","fetch_figure","fetch_table","retrieve"]

    selector = LLMSingleSelector.from_defaults()
    selector_result = selector.select(choices, query="Can you summarize the key takeaways from pages 5-7?")
    print(selector_result.selections)