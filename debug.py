def scrape_flipkart_price(product_name):
    url = "https://www.flipkart.com/search?q=" + product_name
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price_tag = soup.find("div", {"class": "_30jeq3 _1_WHN1"})
    if price_tag is not None:
        price = price_tag.get_text().replace(",", "").replace("₹", "")
        return float(price)
    else:
        return None
import requests
from bs4 import BeautifulSoup

# Function to scrape Amazon prices
def scrape_amazon_price(product_name):
    url = "https://www.amazon.in/s?k=" + product_name
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price_tag = soup.find("span", {"class": "a-price-whole"})
    if price_tag is not None:
        price = price_tag.get_text().replace(",", "")
        return float(price)
    else:
        return None

# Function to scrape Flipkart prices

# Main function to get input from user and scrape prices
def main():
    product_name = input("Enter the product name: ")
    amazon_price = scrape_amazon_price(product_name)
    flipkart_price = scrape_flipkart_price(product_name)
    if amazon_price is not None:
        print("Amazon price:", amazon_price)
    else:
        print("Amazon price not available.")
    if flipkart_price is not None:
        print("Flipkart price:", flipkart_price)
    else:
        print("Flipkart price not available.")

if __name__ == "__main__":
    main()
