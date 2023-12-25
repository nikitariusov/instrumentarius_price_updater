from .classes import Params
import xml.etree.ElementTree as ET
from utils.utils import open_file


def get_settings():
    def setting(tree):
        setting = []
        setting_list = tree.findall('company')
        for i in setting_list:
            setting.append(Params(
                i.find('company_name').text,
                i.find('link').text,
                i.find('offers').text,
                i.find('item_available').text,
                i.find('vendor_Code').text,
                i.find('price').text,
            ))
        return setting

    try:
        tree = ET.parse('setting.xml')
        print(f'Файл с параметрами: setting.xml')
        return setting(tree)
    except:
        try:
            print()
            tree = ET.parse(open_file('setting.xml'))
            return setting(tree)
        except TypeError:
            print("Файл не вибран!")
            exit()
