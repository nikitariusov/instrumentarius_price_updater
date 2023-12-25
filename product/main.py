import requests
import xml.etree.ElementTree as ET
from utils.utils import only_integer
from .classes import Product_item


def load_xml_file(url: str):
    r = requests.get(url)
    print(f'XML link status: {r.status_code}')
    tree = ET.fromstring(requests.get(url).content)
    return tree


def get_price(price, tree, param):
    items_xml = tree.findall(param.offers)  # все товары из XML
    print(f'Количество товаров в прайсе {param.company}: {len(items_xml)}.')

    def get_available(item):
        try:
            return item.find(param.item_available).text
        except AttributeError:
            return item.get(param.item_available)

    for item in items_xml:
        item_available = get_available(item)
        vendor_code = item.find(param.vendor_Code).text
        item_price = only_integer(item.find(param.price).text)

        price[vendor_code] = Product_item(vendor_code, item_price, item_available)
    return price
