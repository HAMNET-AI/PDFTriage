from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
import os
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
from .myJSONQueryEngine import JSONQueryEngine
llm = OpenAI()
dataschema = {
    "description": "data is a structured data book derived from a pdf",
    "type": "object",
    "properties": {
        "headers": {
            "description": "List of contents of each page of the pdf",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "page": {
                        "description": "Page number per pdf page",
                        "type": "integer",
                    },
                    "bbox": {
                        "description": "Bounding box coordinates of the text",
                        "type": "array",
                    },
                    "text": {
                        "description":
                            "Content of the actual text",
                        "type": "string",
                    },
                    "type": {
                        "description":
                            "Structural hierarchy of the text",
                        "type": "string",
                    },
                    "contain_formula": {
                        "description":
                            "Whether the text contains mathematical formulae",
                        "type": "bool",
                    },
                    "font_size": {
                        "description":
                            "Font size of text",
                        "type": "float",
                    },
                    "font_name": {
                        "description":
                            "Font name for text",
                        "type": "string",
                    },
                    "children": {
                        "description":
                            "Child elements of text",
                        "type": "object",
                    },

                },
                "required": ["page", "bbox", "text", "type", "contain_formula", "font_size", "font_name","children"],
            },
        },
    },
    "required": ["headers"]
}
service_context = ServiceContext.from_defaults(llm=llm)
def fetch_pages(query):
    #print("pages")
    with open('F:\code\python\PDFTriage\PDFTriage\data\pdf.json',encoding="utf-8") as pdfdata:
        datapdf = pdfdata.read()
    alldata = json.loads(datapdf)
    data = alldata["data"]
    query_engine = JSONQueryEngine(
        json_value=data,
        json_schema=dataschema,
        service_context=service_context,
        synthesize_response=False,
    )
    query_prompt= f"What contents to the number of pages mentioned in this question : {query}"
    #print(query_prompt)
    josnpath = query_engine.query(query_prompt).metadata['json_path_response_str'].replace("&&", "&")
    jsonpath_expr = parse(josnpath)
    matches = [match.value for match in jsonpath_expr.find(data)]
    print(matches)
def fetch_sections():
    print("Fetching sections")

def fetch_figure():
    print("Fetching figure")

def fetch_table():
    print("fetch_table")

def retrieve():
    print("retrieve")
