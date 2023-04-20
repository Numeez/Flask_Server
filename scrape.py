import requests
from bs4 import BeautifulSoup

def get_ebay_price(product_name):
    # URL for eBay search results for the given product name
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    
    # Send a GET request to the URL and get the HTML response
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first search result on the page
    search_results = soup.find_all('div', {'class': 's-item__wrapper'})
    
    if not search_results:
        return "Sorry, we couldn't find any search results for that product."
    
    # Get the price of the first search result (as a string)
    price_string = search_results[0].find('span', {'class': 's-item__price'}).text
    
    # Remove any non-numeric characters from the price string
    price = ''.join(c for c in price_string if c.isdigit() or c == '.')
    
    return float(price)


print(get_ebay_price("iphone 11"))