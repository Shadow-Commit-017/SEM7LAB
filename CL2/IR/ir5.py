# Step 1: Import libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Step 2: Website URL
url = "https://books.toscrape.com/"

# Step 3: Send request
response = requests.get(url)
response.raise_for_status()

# Step 4: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Extract product information
products = soup.select("article.product_pod")

print("PRODUCT INFORMATION")
print("=" * 50)

# Step 6: Display product details
for i, item in enumerate(products, start=1):

    name = item.select_one("h3 a")["title"]

    price = item.select_one(
        ".price_color"
    ).text.strip()

    rating = item.select_one(
        ".star-rating"
    )["class"][1]

    link = urljoin(
        url,
        item.select_one("h3 a")["href"]
    )

    print("\nProduct:", i)
    print("Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Product Link:", link)
    print("-" * 50)

# Step 7: Display total products
print("\nTotal Products Extracted:", len(products))
print("Crawling Completed Successfully!")
