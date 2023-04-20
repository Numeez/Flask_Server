from flask import Flask,request
import requests,json
from bs4 import BeautifulSoup


app = Flask(__name__)


prices={}

def scrape_flipkart_price(product_name):
    flipkart={"name":"Flipkart"}
    url = "https://www.flipkart.com/search?q=" + product_name
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price_tag = soup.find("div", {"class": "_30jeq3 _1_WHN1"})
    if price_tag is not None:
        price = price_tag.get_text().replace(",", "").replace("₹", "")
        flipkart['price'] = price
        prices['flipkart']=flipkart
    else:
        flipkart['price'] ='Sorry ! not available at this moment'
        prices['flipkart']=flipkart


def scrape_amazon_price(product_name):
    amazon={"name":"Amazon"}
    url = "https://www.amazon.in/s?k=" + product_name
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price_tag = soup.find("span", {"class": "a-price-whole"})
    if price_tag is not None:
        price = price_tag.get_text().replace(",", "")
        amazon['price'] = price
        prices['amazon'] = amazon
    else:
        amazon['price'] = 'Sorry ! Not available at this moment'
        prices['amazon']= amazon


def getSoupObject(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    return soup

def getEbayUrl(name):
    template = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0"
    name = name.replace(" ","+")
    return template.format(name)

def getEbayPrice(name):
    ebay_price={"name":"Ebay"}
    ebay = getSoupObject(getEbayUrl(name))
   
    price = ebay.select('.s-item__price')[1].text
    if(len(name)>0 and len(price)>0):
        
        ebay_price["price"] = price
        prices["ebay"] = ebay_price
    else:
        ebay_price["ebay"] = "This product is not avaliable at this moment"
        prices["ebay"] = ebay_price

@app.route('/products')
def hello_world():
    args = request.args.to_dict()
    product_name = args.get("name")
    getEbayPrice(product_name)
    scrape_amazon_price(product_name)
    scrape_flipkart_price(product_name)
    return prices




    