import json
import os
from src.routers import router
from dotenv import load_dotenv
from jsonpath_ng import jsonpath, parse
from jsonpath_ng.ext import parse
load_dotenv(override=True)

if __name__ == '__main__':
    query = "What is the summary of the contents of table 1"
    router(query=query)
    """path = "$.data[?(@.page >= 5 & @.page <= 7)].boxes[*].text"
    # .replace("&&", "&")
    with open('F:\code\python\PDFTriage\PDFTriage\data\pdf.json', encoding="utf-8") as pdfdata:
        data = json.load(pdfdata)
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    result = [match.value for match in matches]
    print(result)"""