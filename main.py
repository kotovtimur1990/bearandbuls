import os
import telebot
import logging
import psycopg2 #База данных
from config import *
from flask import Flask, request
from telebot import types
import requests


class LIST:
    def __init__(self, msg):
        self.msg = msg
        self.del_pr = None

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

#БАЗА ДАННЫХ
db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()

#БАЗА ДАННЫХ
def update_messages_count(user_id):
    db_object.execute(f"UPDATE users SET messages = messages + 1 WHERE id = {user_id}")
    db_connection.commit()


#@bot.message_handler(commands=["start"])
#def start(message):
#    user_id = message.from_user.id
#    username = message.from_user.username
#    bot.reply_to(message, f"Hello, {username}!")

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
    markup.row(lokaciya)
    bot.reply_to(message, f"Hello, {username}!\n Submit your locality to determine the payment instrument for you", reply_markup=markup)


    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    #one = types.KeyboardButton('Start receiving Forex trading signals')
    #two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
    #sport = types.KeyboardButton('Start receiving sports betting')
    #robot = types.KeyboardButton('Get your Forex trading robot')
    #three = types.KeyboardButton('Information')
    #markup.row(one)
    #markup.row(two)
    #markup.row(sport)
    #markup.row(robot)
    #markup.row(three)
    #bot.send_message(message.chat.id, "Choose one of the following", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Information(message):
    if message.text == "Information":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        Registration = types.KeyboardButton('Registration')
        Back = types.KeyboardButton('Back')
        markup.row(Registration)
        markup.row(Back)
        bot.send_message(message.from_user.id, "Forex and Cryptocurrency Signals.\n"
                                                "Extreme pips \n"
                                                "✅VIP Forex Signals \n"
                                                "✅VIP Cryptocurrency \n"
                                                "Signals +3000 points of estimated profit per month in the channel \n"
                                                "Join us and earn on Forex and Cryptocurrency \n"
                                                "Signals are available after registration and payment. \n"
                                                "Payment is only $2 per week.", reply_markup=markup)
    elif message.text == "Back":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        one = types.KeyboardButton('Start receiving Forex trading signals')
        two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        sport = types.KeyboardButton('Start receiving sports betting')
        robot = types.KeyboardButton('Get your Forex trading robot')
        three = types.KeyboardButton('Information')
        markup.row(one)
        markup.row(two)
        markup.row(sport)
        markup.row(robot)
        markup.row(three)
        bot.send_message(message.chat.id, "Choose one of the following", reply_markup=markup)
    elif message.text == "Registration":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        one = types.KeyboardButton('Start receiving Forex trading signals')
        two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        sport = types.KeyboardButton('Start receiving sports betting')
        robot = types.KeyboardButton('Get your Forex trading robot')
        markup.row(one)
        markup.row(two)
        markup.row(sport)
        markup.row(robot)
        bot.send_message(message.chat.id, "Choose one of the following", reply_markup=markup)
    elif message.text == "Start receiving Forex trading signals":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Submit your locality to determine the payment instrument for you', reply_markup=markup)
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        lokaciya1 = types.InlineKeyboardButton('Submit your locality', callback_data='lokaciya1')
        Back1 = types.InlineKeyboardButton('Main menu', callback_data='menu1')
        markup_inline.add(lokaciya1, Back1)
        bot.send_message(message.chat.id, "👇", reply_markup=markup_inline)
    elif message.text == "Start receiving Cryptocurrency trading signals":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
        Back = types.KeyboardButton('Main menu')
        markup.row(lokaciya)
        markup.row(Back)
        bot.send_message(message.from_user.id, "Submit your locality to determine the payment instrument for you", reply_markup=markup)
    elif message.text == "Start receiving sports betting":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
        Back = types.KeyboardButton('Main menu')
        markup.row(lokaciya)
        markup.row(Back)
        bot.send_message(message.from_user.id, "Submit your locality to determine the payment instrument for you", reply_markup=markup)
    elif message.text == "Get your Forex trading robot":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
        Back = types.KeyboardButton('Main menu')
        markup.row(lokaciya)
        markup.row(Back)
        bot.send_message(message.from_user.id, "Submit your locality to determine the payment instrument for you", reply_markup=markup)
    elif message.text == "Main menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        one = types.KeyboardButton('Start receiving Forex trading signals')
        two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        sport = types.KeyboardButton('Start receiving sports betting')
        robot = types.KeyboardButton('Get your Forex trading robot')
        three = types.KeyboardButton('Information')
        markup.row(one)
        markup.row(two)
        markup.row(sport)
        markup.row(robot)
        markup.row(three)
        bot.send_message(message.chat.id, "Choose one of the following", reply_markup=markup)
    elif message.text == "NO":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
        Back = types.KeyboardButton('Main menu')
        markup.row(lokaciya)
        markup.row(Back)
        bot.send_message(message.from_user.id, "Submit your locality to determine the payment instrument for you", reply_markup=markup)
    elif message.text == "YES":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, ' Pay to start earning ', reply_markup=markup)
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        PAY = types.InlineKeyboardButton('PAY', callback_data='pay1', url='https://paywall.pw/j4xyb8z1mbdl')
        menu1 = types.InlineKeyboardButton('Main menu', callback_data='menu1')
        markup_inline.add(PAY, menu1)
        bot.send_message(message.chat.id, "👇", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'pay1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='SUCCESFULL AR FAILED')
        elif call.data == 'menu1':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            one = types.KeyboardButton('Start receiving Forex trading signals')
            two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
            sport = types.KeyboardButton('Start receiving sports betting')
            robot = types.KeyboardButton('Get your Forex trading robot')
            three = types.KeyboardButton('Information')
            markup_reply.add(one)
            markup_reply.add(two)
            markup_reply.add(sport)
            markup_reply.add(robot)
            markup_reply.add(three)
            bot.send_message(call.message.chat.id, "Choose one of the following", reply_markup=markup_reply)
        elif call.data == 'lokaciya1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='111111111', request_location=True)


@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        coord = str(message.location.longitude) + ',' + str(message.location.latitude)
        r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=4dd7cd0a-35ca-45bc-ac71-fb8f2a9903d3&kind=locality&format=json&lang=en_US&geocode=' + coord)
        if len(r.json()['response']['GeoObjectCollection']['featureMember']) > 0:
            address = \
            r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            YES = types.KeyboardButton('YES')
            NO = types.KeyboardButton('NO')
            markup.row(YES, NO)
            bot.send_message(message.chat.id, 'Your locality:\n{} Do you confirm this ?'.format(address), reply_markup=markup)
            # types.ReplyKeyboardRemove(selective=False)

    else:
        bot.send_message(message.chat.id, 'Failed to get your address')

    # БАЗА ДАННЫХ
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()
    # БАЗА ДАННЫХ
    if not result:
        db_object.execute("INSERT INTO users(id, username, messages) VALUES (%s, %s, %s)", (user_id, username, 0))
        db_connection.commit()

    update_messages_count(user_id)

#БАЗА ДАННЫХ
@bot.message_handler(commands=["stats"])
def get_stats(message):
    db_object.execute("SELECT * FROM users ORDER BY messages DESC LIMIT 10")
    result = db_object.fetchall()

    if not result:
        bot.reply_to(message, "No data...")
    else:
        reply_message = "- Top flooders:\n"
        for i, item in enumerate(result):
            reply_message += f"[{i + 1}] {item[1].strip()} ({item[0]}) : {item[2]} messages.\n"
        bot.reply_to(message, reply_message)

    update_messages_count(message.from_user.id)

#БАЗА ДАННЫХ
@bot.message_handler(func=lambda message: True, content_types=["text"])
def message_from_user(message):
    user_id = message.from_user.id
    update_messages_count(user_id)


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
