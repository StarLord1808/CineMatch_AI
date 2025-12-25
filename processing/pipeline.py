import argparse
import pandas as pd
import json
import os
import glob
from processing.cleaning import clean_text
from processing.embedding import EmbeddingModel
from processing.store import VectorStore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "tests", "output")

def load_metadata(movie_name: str):
    """Finds and loads the JSON metadata file for a movie."""
    # Pattern match for resilience (e.g., checks imdb_data_The_Matrix.json)
    pattern = os.path.join(OUTPUT_DIR, "json", f"imdb_data_{movie_name.replace(' ', '_')}.json")
    files = glob.glob(pattern)
    if not files:
        # Try without replacement or fuzzy if needed, for now strict
        print(f"Metadata file not found for: {pattern}")
        return None
    
    with open(files[0], 'r') as f:
        return json.load(f)

def load_reviews(movie_name: str):
    """Finds and loads the CSV reviews file."""
    pattern = os.path.join(OUTPUT_DIR, "csv", f"imdb_reviews_{movie_name.replace(' ', '_')}.csv")
    files = glob.glob(pattern)
    if not files:
        print(f"Reviews file not found for: {pattern}")
        return None
        
    return pd.read_csv(files[0])

def run_pipeline(movie_name: str):
    print(f"Starting pipeline for: {movie_name}")
    
    # 1. Load Data
    metadata = load_metadata(movie_name)
    reviews_df = load_reviews(movie_name)
    
    if metadata is None or reviews_df is None:
        print("Aborting: Missing data files.")
        return

    # 2. Initialize Models
    embed_model = EmbeddingModel()
    vector_store = VectorStore()
    
    # 3. Process Reviews
    documents = []
    metadatas = []
    
    print(f"Processing {len(reviews_df)} reviews...")
    
    for idx, row in reviews_df.iterrows():
        raw_text = str(row.get('content', ''))
        cleaned_text = clean_text(raw_text)
        
        if len(cleaned_text) < 20:  # Skip very short reviews
            continue
            
        documents.append(cleaned_text)
        
        # Construct metadata
        meta = {
            "source": "imdb",
            "movie_id": metadata.get('imdb_id', 'unknown'),
            "movie_title": metadata.get('title', movie_name),
            "year": str(metadata.get('year', '')),
            "review_title": row.get('title', ''),
            "review_type": row.get('type', 'user'),
            "original_index": idx
        }
        metadatas.append(meta)

    if not documents:
        print("No valid reviews found to process.")
        return

    # 4. Generate Embeddings
    print("Generating embeddings...")
    embeddings = embed_model.encode(documents)
    
    # 5. Store in VectorDB
    print("Storing in ChromaDB...")
    vector_store.add_documents(
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )
    
    print(f"Successfully processed {len(documents)} reviews for {movie_name}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest movie data into Vector DB")
    parser.add_argument("--movie", type=str, required=True, help="Name of the movie (e.g., 'The Matrix')")
    args = parser.parse_args()
    
    run_pipeline(args.movie)
