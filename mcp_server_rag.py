from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from typing import Any

load_dotenv()

def create_retriever() -> Any:
    """
    Create and returns a document retriever based on FAISS vector store.
    
    This function performs the following steps:
    1. Loads a PDF document(place your PDF file in the data folder)
    2. Splits the document into manageable chunks
    3. Creates embeddings for each chunk
    4. Builds a FAISS vector store from the embeddings
    5. Return a retriever interface to ther vector store
    
    Returns: 
        Any: A retrever object that can be used to query the document database.
    """
    # step 1: Load Document
    # PyMyPDFLoader is used to extract text from PDF files
    loader = PyMuPDFLoader("data/DeepSeek-R1.pdf")
    docs = loader.load()
    
    # step 2: Split Document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split_documents = text_splitter.split_documents(docs)
    
    # step 3: Create Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="jhgan/ko-sroberta-multitask")
    
    # step 4: Create FAISS Vector Store
    vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)
    
    # step 5: Create Retriever
    retriever = vectorstore.as_retriever()
    return retriever

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "Retriever",
    instruction="A Retriever that can retrieve information from the database.",
    host="0.0.0.0",
    port=8005,
)

@mcp.tool()
async def retrieve(query: str) -> str:
    """
    Retrieves information from the document database based on the query.
    
    This function creates a retriever, queries it with the provided input,
    and returns the concatenated content of all retrieved documents.
    
    Args:
        query (str): The search query to find relevant information
        
    Returns:
        str: The concatenated content of all retrieved documents.
    """
    
    retriever = create_retriever()
    
    retrieved_docs = retriever.invoke(query)
    
    return "\n".join([doc.page_content for doc in retrieved_docs])

if __name__ == "__main__":
    # Run the FastMCP server
    mcp.run(transport="stdio")