from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
import os
import json
from llama_index.indices.struct_store import JSONQueryEngine
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
    "required": ["headers"],
}
service_context = ServiceContext.from_defaults(llm=llm)
def fetch_pages(query):
    '''with open('F:\code\python\PDFTriage\PDFTriage\data\pdf.json',encoding="utf-8") as pdfdata:
        datapdf = pdfdata.read()
    data = json.loads(datapdf)
    query_engine = JSONQueryEngine(
        json_value=data,
        json_schema=dataschema,
        service_context=service_context,
        synthesize_response=False,
    )
    query_prompt= f"What contents to the number of pages mentioned in this question {query}"
    respones = query_engine.query(query_prompt)
    return respones'''
    json_value = {
        "blogPosts": [
            {
                "id": 1,
                "title": "First blog post",
                "content": "This is my first blog post",
            },
            {
                "id": 2,
                "title": "Second blog post",
                "content": "This is my second blog post",
            },
        ],
        "comments": [
            {
                "id": 1,
                "content": "Nice post!",
                "username": "jerry",
                "blogPostId": 1,
            },
            {
                "id": 2,
                "content": "Interesting thoughts",
                "username": "simon",
                "blogPostId": 2,
            },
            {
                "id": 3,
                "content": "Loved reading this!",
                "username": "simon",
                "blogPostId": 2,
            },
        ],
    }

    # JSON Schema object that the above JSON value conforms to
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "description": "Schema for a very simple blog post app",
        "type": "object",
        "properties": {
            "blogPosts": {
                "description": "List of blog posts",
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "description": "Unique identifier for the blog post",
                            "type": "integer",
                        },
                        "title": {
                            "description": "Title of the blog post",
                            "type": "string",
                        },
                        "content": {
                            "description": "Content of the blog post",
                            "type": "string",
                        },
                    },
                    "required": ["id", "title", "content"],
                },
            },
            "comments": {
                "description": "List of comments on blog posts",
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "description": "Unique identifier for the comment",
                            "type": "integer",
                        },
                        "content": {
                            "description": "Content of the comment",
                            "type": "string",
                        },
                        "username": {
                            "description": (
                                "Username of the commenter (lowercased)"
                            ),
                            "type": "string",
                        },
                        "blogPostId": {
                            "description": (
                                "Identifier for the blog post to which the comment"
                                " belongs"
                            ),
                            "type": "integer",
                        },
                    },
                    "required": ["id", "content", "username", "blogPostId"],
                },
            },
        },
        "required": ["blogPosts", "comments"],
    }
    nl_query_engine = JSONQueryEngine(
        json_value=json_value,
        json_schema=json_schema,
        service_context=service_context,
    )
    nl_response = nl_query_engine.query(
        "What comments has Jerry been writing?",
    )
    print(nl_response)
def fetch_sections():
    print("Fetching sections")

def fetch_figure():
    print("Fetching figure")

def fetch_table():
    print("fetch_table")

def retrieve():
    print("retrieve")
