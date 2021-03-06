import requests
from bs4 import BeautifulSoup
from datetime import date
import re
today = date.today()

# dd/mm/YY
DATE = today.strftime("%Y-%m-%d")


def cleanse(data):
    return re.sub(r"[^a-zA-Z0-9]+", ' ', data).lower()


def remove_after_keyword(data, key):
    return str(data.split(key)[0] if key in data else data)


def replace_ownbrand(data,brand):
    return data.lower().replace(brand, "ownbrand")


def remove_currency(data):
    return data.replace('€',"")


def generate_insert(catagory,item,shop,data,url,brand=None,sku=None):
    print(data)
    price = f"{(data[1].strip())}"
    other = f"{cleanse(data[2].strip())}" if len(data) > 3 else ''
    if(brand == None):
        brand = 'N/A'
    if(sku == None):
        sku = 'N/A'

    # Whenever we get new data with the same URL, we update the price
    rstr = f"INSERT into product values (DEFAULT,'{cleanse(catagory)}','{cleanse(item)}','{shop}','{price}','{DATE}','{brand}','{sku}','{url}','{other}') on conflict(url) do update set price = {price};"

    return rstr

def generate_historical(data,url):
    price = f"{(data[1].strip())}"
    rstr = f"INSERT into historical_prices values (DEFAULT,'{url}','{price}','{DATE}');"
    return rstr


def perform_request(url):
    result = requests.get(url)
    return BeautifulSoup(result.content, "html.parser")