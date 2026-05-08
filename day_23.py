"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""

import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"

def fetch_top_posts():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(HN_URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Network Error \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")
    posts = []

    for post in post_links[:20]:
        title = post.get_text(strip=True)
        url = post.get("href")

        posts.append({
            "Title": title,
            "URL": url
        })

    return posts

def save_to_csv(posts):
    if not posts:
        print("No posts to save.")
        return
    
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "URL"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"Saved Hacker News to {CSV_FILE}")


def main():
    print("Scrapping Hacker News top posts...")
    posts = fetch_top_posts()
    print("Collected top posts, saving to csv...")
    save_to_csv(posts)

if __name__ == "__main__":
    main()