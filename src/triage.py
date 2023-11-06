from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.llms import AzureOpenAI
import httpx
import json, ast
from jsonpath_ng import jsonpath, parse
from jsonpath_ng.ext import parse
from .myJSONQueryEngine import JSONQueryEngine
from dotenv import load_dotenv
import os

load_dotenv(override=True)
dataschema = {
    "description": "This is a request reply containing a parsed pdf file",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "data": {
            "description": "data is a structured data book derived from a pdf",
            "type": "array",
            "items": {
                "type": "object",
                "description": "List of contents of each page of the pdf",
                "properties": {
                    "page": {
                        "description": "Page number of each page",
                        "type": "integer"
                    },
                    "width": {
                        "description": " Width of each page",
                        "type": "integer"
                    },
                    "height": {
                        "description": " Each page of the high",
                        "type": "integer"
                    },
                    "boxes": {
                        "description": "Content block of each page",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "bbox": {
                                    "description": "Bounding box coordinates of the text",
                                    "type": "array",
                                    "items": {
                                        "type": "integer"
                                    }
                                },
                                "text": {
                                    "description": "Content of the block",
                                    "type": "string"
                                },
                                "type": {
                                    "description": "type of the block",
                                    "type": "string"
                                },
                                "index": {
                                    "type": "integer"
                                },
                                "score": {
                                    "type": "number"
                                },
                                "contain_formula": {
                                    "description": "Whether the text contains mathematical formulae",
                                    "type": "boolean"
                                },
                                "font_size": {
                                    "description": "Font size of text",
                                    "type": "number"
                                },
                                "font_name": {
                                    "description": "Font name for text",
                                    "type": "string"
                                }
                            },
                            "required": [
                                "bbox",
                                "text",
                                "type",
                                "index",
                                "score",
                                "contain_formula",
                                "font_size",
                                "font_name"
                            ]
                        }
                    }
                },
                "required": [
                    "page",
                    "width",
                    "height",
                    "boxes"
                ]
            }
        },
        "msg": {
            "type": "string"
        }
    },
    "required": [
        "code",
        "data",
        "msg"
    ]
}
llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),api_base=os.environ.get("OPENAI_API_BASE"))
service_context = ServiceContext.from_defaults(llm=llm)
with open('../data/pdf.json', encoding="utf-8") as pdfdata:
    data = json.load(pdfdata)
query_engine = JSONQueryEngine(
    json_value=data,
    json_schema=dataschema,
    service_context=service_context,
    synthesize_response=False,
)


def fetch_pages(query):
    # print("pages")
    query_prompt = f"What contents to the number of pages mentioned in this question : {query}"
    path = query_engine.query(query_prompt).metadata['json_path_response_str'].replace("&&", "&")
    # path = "$.data[?(@.page >= 5 & @.page <= 7)].boxes[*].text"
    # .replace("&&", "&")
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    content = [match.value for match in matches]
    prompt = f"Please answer a question based on something in the pdf\n, this is the question{query}\n, The contents of the pages mentioned in the question are listed in text as follows {content}"
    response = llm.complete(prompt)
    print(response)



def fetch_sections(query):
    print("Fetching sections")


def fetch_figure():
    print("Fetching figure")


def get_table_num(query):
    prompt = f"""Please indicate in an array form which tables are referred to in a question
              example:
              query : What is the summary of the contents of table 1
              output : [1]
              query : What is the summary of the contents of table 2 and 6" \
              output : [2,6]
              query : What is the summary of the contents of table 2 to 5" \
              output : [2,3,4,5]
              --------------------------------------------------------------\
              this is the question {query} Please indicate in an array form which tables are referred
  """
    response = llm.complete(prompt)
    return response.__str__()
def fetch_table(query):
  query_prompt = f"What contents mentioned in the table of this pdf"
  path = query_engine.query(query_prompt).metadata['json_path_response_str'].replace("&&", "&")
  jsonpath_expression = parse(path)
  matches = jsonpath_expression.find(data)
  result = [match.value for match in matches]
  print("table")
  table_indexs = get_table_num(query)
  table_indexs = ast.literal_eval(table_indexs)
  #content = [result[i] for i in table_indexs]
  content = [f'table{i}:{result[i]}' for i in table_indexs]
  prompt = f"Please answer a question based on something in the pdf\n, this is the question{query}\n, The contents of  tables, mentioned in the question are listed in text as follows {content}"
  response = llm.complete(prompt)
  print(response)


def retrieve():
    print("retrieve")


def pdf_response(query,content):
  print("response")

