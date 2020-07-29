import requests
from lxml import etree, objectify
import datetime

import control_db
import control_tlgm

url = 'https://export.admitad.com/ru/webmaster/websites/1497531/products/export_adv_products/?feed_id=14132&code' \
     '=juvye7j8ok&user=x038xx38%40gmail.com&template=52923'

response = requests.get(url)
xml = response.content

# xml = open('shop.xml', 'rb').read()

tree = etree.fromstring(xml)
offer_list = tree.findall('.//offer[categoryId="1077"]') + tree.findall('.//offer[categoryId="1076"]') + \
             tree.findall('.//offer[categoryId="145"]') + tree.findall('.//offer[categoryId="1075"]') + \
             tree.findall('.//offer[categoryId="1074"]') + tree.findall('.//offer[categoryId="235"]')

# for offer in offer_list:
#     for property in list(offer):
#         print(property.tag, ' ', property.text, ' ', property.attrib)
#     print('-----------------------------')


def get_value(obj, element, attrib=False):
    value = ''
    try:
        list = obj.findall(element)
        for node in list:
            if attrib:
                value = value + node.attrib['name'] + ': ' + node.text + '\n'
            else:
                value = value + node.text + '\n'
    except AttributeError as e:
        print(e)
        print(obj.attrib)
    return value


count = 0

now = datetime.datetime.fromtimestamp(datetime.datetime.today().timestamp())
delta = datetime.timedelta(days=1)
period = now - delta
period = period.timestamp()

for offer in offer_list:
    # price = offer.find('price').text
    # price = float(price)

    modified_time = get_value(offer, 'modified_time')

    if float(modified_time)-period >= 0:
        timestamp = datetime.datetime.fromtimestamp(float(modified_time))
        modified_time = timestamp.strftime('%Y-%m-%d %H:%M')

        categoryId = get_value(offer, 'categoryId')
        vendor = get_value(offer, 'vendor')
        name = get_value(offer, 'name')
        description = get_value(offer, 'description')
        description = description.replace('\\', '\n')

        param = get_value(offer, 'param', attrib=True)

        # params = offer.findall('param')
        # for param in params:
        #     print(param.attrib['name'] + ': ' + param.text)
        #
        # exit()

        picture = get_value(offer, 'picture')
        old_price = get_value(offer, 'oldprice')
        price = get_value(offer, 'price')
        url = get_value(offer, 'url')

        row = (modified_time, categoryId, vendor, name, description, param, picture, old_price, price, url)
        conn = control_db.create_connection('database.db')
        control_db.add_offer(conn, row)

        control_tlgm.send_message(row)

        print('Norma')

        count += 1
        # if count > 5:
        #     exit()

    else:
        print('No norma')





print('Общее количество записей - ', count)




