# examples/basic_rag/app.py

from ragstack.rag.pipeline import RAGPipeline
from ragstack.data.connectors.file_system import FileSystemConnector
from ragstack.vectorstores.inmemory import InMemoryVectorStore
from ragstack.llm.dummy import DummyLLM

def main():
    # Set up components
    data_connector = FileSystemConnector("data.txt")
    vector_store = InMemoryVectorStore()
    llm = DummyLLM()

    # Create RAG pipeline
    rag_pipeline = RAGPipeline(
        retriever=vector_store,
        llm=llm,
        prompt_template="{query}\n\nContext: {context}"
    )

    # Fetch and index data
    data = data_connector.fetch_data()
    vector_store.index([data])

    # Run a query
    query = "What is RAG?"
    response = rag_pipeline.run(query)
    print(f"Query: {query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()