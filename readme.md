## PDFTriage: Question Answering over Long, Structured Documents

# PDFtriage

PDFtriage: 用于结构化文档问答的新方法，提供了基于结构和内容的上下文检索，解决了现有模型在处理结构化文档时的局限性

## Dependencies

- llama-index==0.8.56

## Usage

1. **Scan and Parse PDF Files**

   首先，你需要将你的PDF文件扫描并解析为JSON格式。你可以使用以下网址将你的PDF文件解析为JSON数据：https://apifox.com/apidoc/shared-a55f1a3d-4871-41b7-8f1a-3af83807410b/api-120356017

2. **Set Environment Variables**

   在使用 PDFtriage 之前，你需要设置一些环境变量。你可以在 .env.example 文件中找到示例，并按照相同的格式创建一个 .env 文件。以下是需要设置的环境变量：

   ```plaintext
   OPENAI_API_KEY=Your_OpenAI_API_Key
   OPENAI_API_BASE=API_Base_URL
   FILE_PATH=Path_to_the_JSON_Data_File_of_the_Parsed_PDF
## Example

在设置好环境变量之后，你可以按照以下示例使用 PDFtriage：
``` plaintext
query = "What is the summary of the contents of table 1"
result = router(query=query)
print("Output:", result)  
```

运行以上代码，你将得到类似如下的输出：
``` plaintext
"The summary of the contents of table 1 is as follows:

- Positive triple: (Los Angeles, LocatedIn, California)
- Negative sampling
  - High-quality negative triple: (Los Angeles, LocatedIn, Georgia)
  - False-negative triples: (Apple Inc., LocatedIn, California), (Los Angeles, LocatedIn, Apple Pie)
  - Low-quality negative triples: (English, LocatedIn, California)
- Challenge 1: Invalid Negative Sampling
  - Query: (David, Nationality, ?)
  - Correct triple: (David, Nationality, U.S.A.)
  - Rank: Commonsense California 11, California Unsatisfy, David+rNationality-eCalifornia 2, U.S.A. Satisfy, David+rNationality-eU.S.A. 3
- Challenge 2: Uncertainty of Fact-View Link Prediction
  - Figure 1: Two examples exhibit the challenges that needed to be addressed.
  - Challenge 1: Given a positive triple, some generated negative triples are false negative or low-quality.
  - Challenge 2: For link prediction, the entity ranks higher than the correct entity U.S.A. due to the uncertainty of KG embeddings, but the correct answer entity should belong to the concept Country in the view of commonsense.
Process finished with exit code 0"
```
