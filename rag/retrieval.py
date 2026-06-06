from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def retrieve_chunks(query: str,k:int=3):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Same embedding model used while creating vector DB
    vector_db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    
    
    results = vector_db.similarity_search(
        query=query,
        k=k
    )
    
    return results


if __name__ == "__main__":

    query = input("Enter your query: ")

    retrieved_docs = retrieve_chunks(query)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(retrieved_docs, start=1):

        print(f"\n{'=' * 50}")
        print(f"Chunk {i}")
        print(f"{'=' * 50}")

        print(doc.page_content)