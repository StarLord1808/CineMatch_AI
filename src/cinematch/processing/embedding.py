from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingModel:
    """
    Wrapper for sentence-transformers model to generate text embeddings.
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the embedding model.
        Args:
            model_name: The name of the HuggingFace model to use.
        """
        print(f"Loading embedding model: {model_name}...")
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of strings to embed.
            
        Returns:
            List of embedding vectors (list of floats).
        """
        # Convert numpy array to list for JSON serialization compatibility if needed
        embeddings = self.model.encode(texts)
        return embeddings.tolist()
