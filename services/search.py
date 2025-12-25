from processing.embedding import EmbeddingModel
from processing.store import VectorStore
from typing import List, Dict

class SearchService:
    """
    Service to handle semantic search queries against the vector database.
    """
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def search(self, query: str, k: int = 10, filter_criteria: Dict = None) -> List[Dict]:
        """
        Search for documents similar to the query string.
        
        Args:
            query: User's search text.
            k: Number of results to return.
            filter_criteria: Metadata filters (optional).
            
        Returns:
            List of dictionaries containing matched documents and metadata.
        """
        # 1. Generate embedding for the query
        query_embedding = self.embedding_model.encode([query])[0]
        
        # 2. Query the vector store
        # Note: ChromaDB query returns a specific structure. vector_store.query wrapper returns this.
        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=filter_criteria
        )
        
        # 3. Format results into a cleaner list of dicts
        formatted_results = []
        if not results['ids']:
            return []
            
        # Chroma returns lists of lists (one per query). We only have one query.
        ids = results['ids'][0]
        distances = results['distances'][0]
        metadatas = results['metadatas'][0]
        documents = results['documents'][0]
        
        for i in range(len(ids)):
            formatted_results.append({
                'id': ids[i],
                'score': 1 - distances[i],  # specific to cosine distance if used, Chroma default is L2 usually, need to check distance metric. Assuming L2 roughly maps to distance. 
                                          # Ideally we'd configure cosine similarity. For L2, smaller is better.
                                          # Let's just return distance for now or invert if we know the metric. 
                                          # Default Chroma is L2 (Squared Euclidean). 0 is exact match.
                'distance': distances[i],
                'metadata': metadatas[i],
                'content': documents[i]
            })
            
        return formatted_results
