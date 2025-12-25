import chromadb
import uuid
from typing import List, Dict, Optional
import os

class VectorStore:
    """
    Wrapper for ChromaDB to manage vector storage and retrieval.
    """
    def __init__(self, collection_name: str = "cinematch_reviews", persistent_path: str = "./data/chroma_db"):
        """
        Initialize ChromaDB client and collection.
        
        Args:
            collection_name: Name of the collection to use.
            persistent_path: Path to store database files.
        """
        # Ensure data directory exists
        os.makedirs(persistent_path, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=persistent_path)
        self.collection = self.client.get_or_create_collection(name=collection_name)
        print(f"Connected to ChromaDB collection: {collection_name}")

    def add_documents(self, documents: List[str], metadatas: List[Dict], embeddings: Optional[List[List[float]]] = None, ids: Optional[List[str]] = None):
        """
        Add documents to the collection.
        
        Args:
            documents: List of text content.
            metadatas: List of metadata dictionaries.
            embeddings: Optional list of embedding vectors.
            ids: Optional list of unique IDs.
        """
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(documents))]
            
        if not documents:
            return

        self.collection.upsert(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Upserted {len(documents)} documents to {self.collection.name}")

    def query(self, query_text: str, n_results: int = 5, where: Optional[Dict] = None):
        """
        Query the collection for similar documents.
        
        Args:
            query_text: The search query text.
            n_results: Number of results to return.
            where: Optional filtering criteria (e.g., {"year": "1999"}).
            
        Returns:
            Query results dictionary.
        """
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=where
        )

    def count(self):
        """Return total number of documents in collection."""
        return self.collection.count()
    
    def peek(self, limit: int = 5):
        """Return first N documents."""
        return self.collection.peek(limit=limit)
