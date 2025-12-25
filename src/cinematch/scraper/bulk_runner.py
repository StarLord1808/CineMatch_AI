import argparse
import time
import random
import requests
from bs4 import BeautifulSoup
from cinematch.scraper.imdb_scraper import IMDbScraperDDGS
from pathlib import Path
from typing import List

class BulkScraper:
    def __init__(self):
        self.scraper = IMDbScraperDDGS()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    def fetch_top_movies(self, limit: int = 50) -> List[str]:
        """
        Fetches movie titles from IMDb Top 250.
        """
        print("📊 Fetching Top Generic Movies List (IMDb chart)...")
        url = "https://www.imdb.com/chart/top/"
        titles = []
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Modern IMDb Chart Selectors
            # Look for <h3> inside logic (ipc-title__text)
            title_elements = soup.select('h3.ipc-title__text')
            
            for elem in title_elements:
                text = elem.get_text(strip=True)
                # Format is usually "1. The Shawshank Redemption"
                if '.' in text:
                    parts = text.split('.', 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        title = parts[1].strip()
                        titles.append(title)
                        
                if len(titles) >= limit:
                    break
                    
            if not titles:
                # Fallback list if scraping fails (anti-bot)
                print("⚠️ Scraping chart failed or blocked. Using fallback list.")
                titles = [
                    "The Shawshank Redemption", "The Godfather", "The Dark Knight",
                    "Schindler's List", "12 Angry Men", "Pulp Fiction",
                    "The Lord of the Rings: The Return of the King", "The Good, the Bad and the Ugly",
                    "Fight Club", "Forrest Gump", "Inception", "The Matrix",
                    "Goodfellas", "One Flew Over the Cuckoo's Nest", "Seven",
                    "Interstellar", "Parasite", "Whiplash"
                ][:limit]
                
        except Exception as e:
            print(f"❌ Error fetching chart: {e}")
            titles = ["The Matrix", "Inception", "Interstellar"][:limit] # Minimal fallback
            
        print(f"✅ Found {len(titles)} titles to scrape.")
        return titles

    def run(self, limit: int = 10, delay_range: tuple = (2, 5)):
        """
        Run the bulk scraping process.
        """
        print(f"🚀 Starting Bulk Scrape (Limit: {limit})")
        
        # 1. Get List
        titles = self.fetch_top_movies(limit)
        
        # 2. Iterate
        for i, title in enumerate(titles, 1):
            print(f"\n[{i}/{len(titles)}] Processing: {title}")
            
            try:
                # Check for existing
                safe_title = title.replace(' ', '_')
                if Path(f"data/json/imdb_data_{safe_title}.json").exists():
                    print(f"⏭️  Skipping {title} (Already exists)")
                    continue
                
                # Scrape
                data = self.scraper.scrape_comprehensive_movie_data(title)
                
                if 'error' not in data:
                    self.scraper.save_movie_data(data, format='both')
                else:
                    print(f"❌ Failed to scrape {title}: {data['error']}")
                
                # Respectful Delay
                sleep_time = random.uniform(*delay_range)
                print(f"💤 Sleeping for {sleep_time:.1f}s...")
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"❌ Critical error on {title}: {e}")
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk scrape IMDb movies")
    parser.add_argument("--limit", type=int, default=10, help="Number of movies to scrape")
    args = parser.parse_args()
    
    scraper = BulkScraper()
    scraper.run(limit=args.limit)
