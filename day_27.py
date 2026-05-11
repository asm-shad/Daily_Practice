"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.
"""

import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []

    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text

        quote_data.append((text, author))

    return quote_data

def create_image(text, author, index):
    width, height = 1000, 600

    # Colors
    background_color = "#f7cf61"
    text_color = "#222222"
    author_color = "#444444"

    # Create Image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Better Fonts
    # Windows font paths
    quote_font = ImageFont.truetype(
        "C:/Windows/Fonts/georgia.ttf", 40
    )

    author_font = ImageFont.truetype(
        "C:/Windows/Fonts/ariali.ttf", 28
    )

    # Add quotation marks
    quote = f'“{text}”'

    # Wrap text properly
    wrapped_text = textwrap.fill(quote, width=28)

    # Get text bounding box
    bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped_text,
        font=quote_font,
        spacing=15
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center quote block
    x_text = (width - text_width) / 2
    y_text = (height - text_height) / 2 - 40

    # Draw quote
    draw.multiline_text(
        (x_text, y_text),
        wrapped_text,
        font=quote_font,
        fill=text_color,
        spacing=15,
        align="center"
    )

    # Author text
    author_text = f"— {author}"

    author_bbox = draw.textbbox(
        (0, 0),
        author_text,
        font=author_font
    )

    author_width = author_bbox[2] - author_bbox[0]

    # Center author
    x_author = (width - author_width) / 2
    y_author = y_text + text_height + 40

    draw.text(
        (x_author, y_author),
        author_text,
        font=author_font,
        fill=author_color
    )

    # Create output folder
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Save image
    filename = os.path.join(
        OUTPUT_DIR,
        f"quote_{index+1}.png"
    )

    image.save(filename)

    print(f"Saved: {filename} ✅")

def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)

if __name__ == "__main__":
    main()