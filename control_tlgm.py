import telegram

token = ''
bot = telegram.Bot(token)
user_id = 0

def send_message(offer, b=bot, us_id=user_id):
    modified_time, categoryId, vendor, name, description, param, picture, old_price, price, url = offer
    html_msg = '<b>Дата оффера:</b> {}\n<b>Продавец:</b> {}\n<b>Продукт:</b> {}\n<b>Описание:</b>\n{}\n' \
               '<b>Параметры:</b>\n{}\n<b>Изображения:</b>\n{}\n<b>Старая цена:</b> {}\n<b>Новая цена:</b> {}\n' \
               ''.format(modified_time, vendor, name, description, param, picture, old_price, price)
    b.send_message(user_id, html_msg, parse_mode=telegram.ParseMode.HTML)
    pass


# pic = ['https://superstep.ru/upload/photo/1476/TMFW0FW04312990.jpg',
#          'https://superstep.ru/upload/photo/1476/TMFW0FW04312CKI.jpg']
# media = [telegram.InputMediaPhoto(url) for url in pic]
# bot.send_media_group(user_id, media=media)