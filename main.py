from src.routers import router
import os,json
from dotenv import load_dotenv

load_dotenv( override=True)

if __name__ == '__main__':
    query = "Can you summarize the key takeaways from pages 5-7?"
    router(query=query)
    # '''with open('F:\code\python\PDFTriage\PDFTriage\data\pdf.json',encoding="utf-8") as pdfdata:
    #     datapdf = pdfdata.read()
    # data = json.loads(datapdf)
    # print(data.get("headers", {}))'''

# '''    # choices as a list of tool metadata
#     choices = [
#         ToolMetadata(description="Get the text contained in the pages listed", name="fetch_pages"),
#         ToolMetadata(description="Get the text contained in the section listed", name="fetch_sections"),
#         ToolMetadata(description="Get the text contained in the figure caption listed", name="fetch_figure"),
#         ToolMetadata(description="Get the text contained in the table caption listed", name="fetch_table"),
#         ToolMetadata(description="Issue a natural language query over the document, and fetch relevant chunks.", name="retrieve"),
#     ]
#
#     # choices as a list of strings
#     #choices = ["fetch_pages", "fetch_sections","fetch_figure","fetch_table","retrieve"]
#
#     selector = LLMSingleSelector.from_defaults()
#     selector_result = selector.select(choices, query="Can you summarize the key takeaways from pages 5-7?")
#     print(selector_result.selections)'''
