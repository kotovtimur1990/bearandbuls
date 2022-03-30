import os
import telebot
from telebot import types
import logging
from flask import Flask, request
bot = telebot.TeleBot ('5267048474:AAFWZRQqCwIuZ15123123PzJkj3OR8BiGVH8KEXrM')
APP_URL = "https://bearandbuls.herokuapp.com/" + bot

bot = telebot.TeleBot(bot)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

#@bot.message.hendler(commands=["start"])
#def start(message):
#    username = message.from_user.username
#    bot.reply_to(message, f"Hello, {username}!")

#@server.route(f"/{BOT_TOKEN}", methods=["POST"])
#def redirect_message():
#    json_string = request.get_data().decode("utf-8")
#    update = telebot.types.Update.de_json(json_string)
#    bot.process_new_updates([update])
#    return "!", 200
apikey = ('4dd7cd0a-35ca-45bc-ac71-fb8f2a9903d3')


@bot.message_handler(content_types=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu = types.KeyboardButton('Меню')
    moizakazi = types.KeyboardButton('Моизаказы')
    ostavit_otziv = types.KeyboardButton('Оставитьотзыв')
    Nastroiki = types.KeyboardButton('Настройки')
    markup.row(menu)
    markup.row(moizakazi)
    markup.row(ostavit_otziv, Nastroiki)
    bot.send_message(message.chat.id, "Выберите одно из следующих", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def Меню(message):
    if message.text == "Меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        moiadresa = types.KeyboardButton('Мои адреса')
        nazad = types.KeyboardButton('Назад.')
        markup.row(lokaciya)
        markup.row(moiadresa, nazad)
        bot.send_message(message.from_user.id, "Отправьте свою геопозицию", reply_markup=markup)

    elif message.text == "Нет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        moiadresa = types.KeyboardButton('Мои адреса')
        nazad = types.KeyboardButton('Назад.')
        markup.row(lokaciya)
        markup.row(moiadresa, nazad)
        bot.send_message(message.from_user.id, "Отправьте свою геопозицию", reply_markup=markup)
    elif message.text == "Да":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Set = types.KeyboardButton('Сет')
        Lavash = types.KeyboardButton('Лаваш')
        Shaurma = types.KeyboardButton('Шаурма')
        Donar = types.KeyboardButton('Донар')
        Burger = types.KeyboardButton('Бургер')
        Hotdog = types.KeyboardButton('Хот-дог')
        Deserti = types.KeyboardButton('Десерты')
        Napitki = types.KeyboardButton('Напитки')
        Garnir = types.KeyboardButton('Гарнир')
        Korzina = types.KeyboardButton('Корзина')
        Nazad = types.KeyboardButton('Назад')
        markup.row(Set, Lavash)
        markup.row(Shaurma, Donar)
        markup.row(Burger, Hotdog)
        markup.row(Burger, Hotdog)
        markup.row(Deserti, Napitki)
        markup.row(Garnir)
        markup.row(Korzina, Nazad)
        bot.send_message(message.from_user.id, "Выберите категорию", reply_markup=markup)
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        moiadresa = types.KeyboardButton('Мои адреса')
        nazad = types.KeyboardButton('Назад.')
        markup.row(lokaciya)
        markup.row(moiadresa, nazad)
        bot.send_message(message.from_user.id, "Отправьте свою геопозицию", reply_markup=markup)
    elif message.text == "Назад.":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        moizakazi = types.KeyboardButton('Моизаказы')
        ostavit_otziv = types.KeyboardButton('Оставитьотзыв')
        Nastroiki = types.KeyboardButton('Настройки')
        markup.row(menu)
        markup.row(moizakazi)
        markup.row(ostavit_otziv, Nastroiki)
        bot.send_message(message.chat.id, "Выберите одно из следующих", reply_markup=markup)
    elif message.text == "Моизаказы":
        bot.send_message(message.from_user.id, "Номер заказа: 6197454 Статус: Заказ передан клиенту - API Адрес: Узбекистан, Ташкент, Юнусабадский район, махалля Отчопар-2 1️⃣ ✖️ Пепси 1,5л 1️⃣ ✖️ FITTER 1️⃣ ✖️ Калампир лаваш куриный 2️⃣ ✖️ Донар Тип оплаты: Payme Товары: 128 000 сум Доставка: 9 000 сум Итого: 137 000 сум")
    elif message.text == "Оставитьотзыв":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        nazad = types.KeyboardButton('Назад.')
        markup.row(nazad)
        bot.send_message(message.from_user.id, "Отправьте ваши отзывы", reply_markup=markup)
    elif message.text == "Настройки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        izmeniyyazik = types.KeyboardButton('Изменить язык')
        markup.row(izmeniyyazik)
        bot.send_message(message.from_user.id, "Выберите действие:", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        moizakazi = types.KeyboardButton('Моизаказы')
        ostavit_otziv = types.KeyboardButton('Оставитьотзыв')
        Nastroiki = types.KeyboardButton('Настройки')
        markup.row(menu)
        markup.row(moizakazi)
        markup.row(ostavit_otziv, Nastroiki)
        bot.send_message(message.chat.id, "Выберите одно из следующих", reply_markup=markup)


@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
       coord = str(message.location.longitude) + ',' + str(message.location.latitude)
       r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=4dd7cd0a-35ca-45bc-ac71-fb8f2a9903d3&format=json&geocode='+coord)
       if len(r.json()['response']['GeoObjectCollection']['featureMember']) > 0:
            address = r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData']['text']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            DA = types.KeyboardButton('Да')
            NET = types.KeyboardButton('Нет')
            markup.row(DA, NET)
            bot.send_message(message.chat.id, 'Адрес, по которому вы хотите заказать:\n{} Вы подтверждаете этот адрес?'.format(address), reply_markup=markup)
       else:
            bot.send_message(message.chat.id, 'Не удалось получить Ваш адрес')

bot.polling(none_stop=True)


if __name__ == "__main__":
    bot.remove.webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
