import requests
from scraper.utils import get_headers

url = "https://www.imdb.com/title/tt1375666/reviews"
headers = get_headers()
print("Fetching:", url)
resp = requests.get(url, headers=headers)
print("Status:", resp.status_code)

with open("reviews_debug.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
print("Saved to reviews_debug.html")
