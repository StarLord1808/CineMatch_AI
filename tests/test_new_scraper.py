from cinematch.scraper.imdb_scraper import IMDbScraperDDGS
import json
from pathlib import Path

def test_scraper():
    print("Testing IMDbScraperDDGS...")
    scraper = IMDbScraperDDGS()
    
    # Test movie: The Matrix (1999)
    movie_title = "The Matrix"
    print(f"Scraping data for: {movie_title}")
    
    data = scraper.scrape_comprehensive_movie_data(movie_title)
    
    if 'error' in data:
        print(f"❌ Verification failed: {data['error']}")
        return
    
    print("\n✅ Scraping successful!")
    print(f"Title: {data.get('title')}")
    print(f"Year: {data.get('year')}")
    print(f"IMDb ID: {data.get('imdb_id')}")
    
    # Verify critical fields
    required_fields = ['title', 'year', 'cast', 'user_reviews', 'featured_reviews']
    missing = [f for f in required_fields if f not in data or not data[f]]
    
    if missing:
        print(f"⚠️ Warning: Missing some fields: {missing}")
    else:
        print("✅ All critical fields present.")

    # Test saving
    print("\nTesting save functionality...")
    save_path = Path("tests/output")
    scraper.save_movie_data(data, file_location=save_path)
    
    expected_json = save_path / "json" / "imdb_data_The_Matrix.json"
    if expected_json.exists():
        print(f"✅ File saved successfully at {expected_json}")
    else:
        print(f"❌ File saving failed. {expected_json} not found.")

if __name__ == "__main__":
    test_scraper()
