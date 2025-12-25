"""
test_scraper_manual.py
----------------------

This is a manual verification script to test the IMDbScraper class.
It runs the scraper against a specific movie URL and prints the results to the console.

Usage:
    python -m tests.test_scraper_manual
"""

from cinematch.scraper.imdb_scraper import IMDbScraper

def main():
    """
    Main function to execute the manual test.
    """
    # 1. Instantiate the scraper
    print("Initializing Scraper...")
    scraper = IMDbScraper()

    # 2. Define a test target (Inception is a good baseline)
    # Using 'tt1375666' which is the ID for Inception (2010)
    test_url = "https://www.imdb.com/title/tt1375666/"
    print(f"Targeting Movie: {test_url}")

    # 3. Test Metadata Extraction
    print("\n--- Fetching Metadata ---")
    metadata = scraper.get_movie_metadata(test_url)
    
    if metadata:
        print("SUCCESS! Metadata found:")
        print(f"  Title: {metadata.get('title')}")
        print(f"  Year:  {metadata.get('year')}")
        print(f"  Rate:  {metadata.get('rating')}")
        print(f"  Plot:  {metadata.get('plot')[:100]}...") # truncate for display
    else:
        print("FAILED to fetch metadata.")

    # 4. Test Review Extraction
    print("\n--- Fetching Reviews ---")
    reviews = scraper.get_reviews(test_url, max_count=3)
    
    if reviews:
        print(f"SUCCESS! Fetched {len(reviews)} reviews:")
        for i, rev in enumerate(reviews, 1):
            print(f"\n  Review #{i}")
            print(f"  Title: {rev['title']}")
            print(f"  Score: {rev['score']}")
            print(f"  Text:  {rev['text'][:80]}...") # truncate
    else:
        print("FAILED (or empty) reviews found.")

if __name__ == "__main__":
    main()
