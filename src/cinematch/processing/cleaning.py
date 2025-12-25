import re
import html

def clean_text(text: str) -> str:
    """
    Cleans and normalizes text for embedding.
    
    Args:
        text: Raw text input.
        
    Returns:
        Cleaned text string.
    """
    if not text:
        return ""
    
    # Decode HTML entities (e.g., &quot; -> ")
    text = html.unescape(text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    
    # Remove multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def chunk_text(text: str, max_words: int = 500) -> list[str]:
    """
    Splits text into smaller chunks for embedding models that have token limits.
    Simple word-based chunking.
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
        
    return chunks
