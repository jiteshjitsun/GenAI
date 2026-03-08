from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learining_rag",
    embedding=embedding_model
)

user_query = input("Ask something...")


# relevant chunks from vector db

search_result = vector_db.similarity_search(query=user_query)

context = "\n\n".join([f"Page content: {result.page_content}\nPage Number: {result.metadata['page']}\nFile Location: {result.metadata['source']}"
                         for result in search_result])

SYSTEM_PROMT = """
    You are a helpful AI assistant who answers user query base on the available context
    retrieved from a pdf file along with page_contents and page number.
    
    You should only answer the user based on the following context and navigate the user to open the
    right page number to know more.
    
    Context:
    {context}
""".format(context=context)
response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": SYSTEM_PROMT},
        {"role": "user", "content": user_query}
    ]
)

print(f" >>> {response.choices[0].message.content}")