import os
import telebot
import logging
#import psycopg2 #База данных
from config import *
from flask import Flask, request
from telebot import types
import requests


#class LIST:
#    def __init__(self, msg):
#        self.msg = msg
#        self.del_pr = None

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

#БАЗА ДАННЫХ
#db_connection = psycopg2.connect(DB_URI, sslmode="require")
#db_object = db_connection.cursor()

#БАЗА ДАННЫХ
#def update_messages_count(user_id):
#    db_object.execute(f"UPDATE users SET messages = messages + 1 WHERE id = {user_id}")
#    db_connection.commit()


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
    bot.reply_to(message, f"Hello, {username}!\n \n \nSubmit your locality to determine the payment instrument for you", reply_markup=markup)


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
    #elif message.text == "Back":
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
    #elif message.text == "Registration":
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        #one = types.KeyboardButton('Start receiving Forex trading signals')
        #two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        #sport = types.KeyboardButton('Start receiving sports betting')
        #robot = types.KeyboardButton('Get your Forex trading robot')
        #markup.row(one)
        #markup.row(two)
        #markup.row(sport)
        #markup.row(robot)
        #bot.send_message(message.chat.id, "Choose one of the following", reply_markup=markup)
    elif message.text == "Start receiving Forex trading signals":
        #markup = types.ReplyKeyboardRemove(selective=False)
        #bot.send_message(message.chat.id, 'Choose the following', reply_markup=markup)
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        PAY1 = types.InlineKeyboardButton('PAY', callback_data='PAY1', url='https://paywall.pw/j4xyb31zvxdl')
        INFO1 = types.InlineKeyboardButton('Information', callback_data='INFO1')
        #Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(PAY1, INFO1)
        #markup_inline.add(Back)
        bot.send_message(message.chat.id, "Choose the following", reply_markup=markup_inline)
    elif message.text == "Start receiving Cryptocurrency trading signals":
        #markup = types.ReplyKeyboardRemove(selective=False)
        #bot.send_message(message.chat.id, 'Choose the following', reply_markup=markup)
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        PAY2 = types.InlineKeyboardButton('PAY', callback_data='PAY2', url='https://paywall.pw/7e6vmbgl1pdg')
        INFO2 = types.InlineKeyboardButton('Information', callback_data='INFO2')
        #Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(PAY2, INFO2)
        #markup_inline.add(Back)
        bot.send_message(message.chat.id, "Choose the following", reply_markup=markup_inline)
    #elif message.text == "Start receiving sports betting":
        #markup = types.ReplyKeyboardRemove(selective=False)
        #bot.send_message(message.chat.id, 'Choose the following', reply_markup=markup)
        #markup_inline = types.InlineKeyboardMarkup(row_width=2)
        #PAY3 = types.InlineKeyboardButton('PAY', callback_data='PAY3', url='https://paywall.pw/y3xjpy1jl464')
        #INFO3 = types.InlineKeyboardButton('Information', callback_data='INFO3')
        #Back = types.InlineKeyboardButton('Back', callback_data='Back')
        #markup_inline.add(PAY3, INFO3)
        #markup_inline.add(Back)
        #bot.send_message(message.chat.id, "Choose the following", reply_markup=markup_inline)
    elif message.text == "Get your Forex trading robot":
        #markup = types.ReplyKeyboardRemove(selective=False)
        #bot.send_message(message.chat.id, 'Choose the following', reply_markup=markup)
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        PAY4 = types.InlineKeyboardButton('PAY', callback_data='PAY4', url='https://paywall.pw/8k6mlzrmqjdo')
        INFO4 = types.InlineKeyboardButton('Information', callback_data='INFO4')
        #Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(PAY4, INFO4)
        #markup_inline.add(Back)
        bot.send_message(message.chat.id, "Choose the following", reply_markup=markup_inline)
    #elif message.text == "Return":
    #elif message.text == "Return":
    #elif message.text == "Return":
    #elif message.text == "Return":
    elif message.text == "NO":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lokaciya = types.KeyboardButton(text="Submit your locality", request_location=True)
        markup.row(lokaciya)
        bot.reply_to(message, f"Submit your locality to determine the payment instrument for you", reply_markup=markup)

    elif message.text == "YES":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        one = types.KeyboardButton('Start receiving Forex trading signals')
        two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        #sport = types.KeyboardButton('Start receiving sports betting')
        robot = types.KeyboardButton('Get your Forex trading robot')
        markup.row(one)
        markup.row(two)
        #markup.row(sport)
        markup.row(robot)
        bot.send_message(message.chat.id, "GREAT! \n \nChoose how would you like to earn?", reply_markup=markup)



        #markup = types.ReplyKeyboardRemove(selective=False)
        #bot.send_message(message.chat.id, ' Pay to start earning ', reply_markup=markup)
        #markup_inline = types.InlineKeyboardMarkup(row_width=2)
        #PAY = types.InlineKeyboardButton('PAY', callback_data='pay1', url='https://paywall.pw/j4xyb8z1mbdl')
        #menu1 = types.InlineKeyboardButton('Main menu', callback_data='menu1')
        #markup_inline.add(PAY, menu1)
        #bot.send_message(message.chat.id, "👇", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda callback: callback.data)
def chek_callback_data(callback):
    if callback.data == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        one = types.KeyboardButton('Start receiving Forex trading signals')
        two = types.KeyboardButton('Start receiving Cryptocurrency trading signals')
        #sport = types.KeyboardButton('Start receiving sports betting')
        robot = types.KeyboardButton('Get your Forex trading robot')
        markup.row(one)
        markup.row(two)
        #markup.row(sport)
        markup.row(robot)
        bot.send_message(callback.message.chat.id, "Choose how would you like to earn?", reply_markup=markup)
    elif callback.data == 'INFO1':
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        Join1 = types.InlineKeyboardButton('Join a channel', url='https://paywall.pw/j4xyb31zvxdl')
        Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(Join1, Back)
        bot.send_message(callback.message.chat.id, "Our team uses a variety of trading methods and provides quality signals that are carefully thought out and carry the least risk. In our channel, we give from 3 to 6 signals per day, the success rate of which is more than 85%, and our monthly goal is above 2000 points.✅✅✅", reply_markup=markup_inline)
    elif callback.data == 'INFO2':
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        Join1 = types.InlineKeyboardButton('Join a channel', url='https://paywall.pw/7e6vmbgl1pdg')
        Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(Join1, Back)
        bot.send_message(callback.message.chat.id, "We offer cryptocurrency trading signals that will help you generate and bring good income by trading a wide range of instrument categories. Our team has qualified financiers/traders who analyze the market and provide signals especially for you. In our channel, we give from 3 to 5 signals per day, the success of which is more than 90% ✅✅✅", reply_markup=markup_inline)
    #elif callback.data == 'INFO3':
        #markup_inline = types.InlineKeyboardMarkup(row_width=2)
        #Join1 = types.InlineKeyboardButton('Join a channel', url='https://paywall.pw/y3xjpy1jl464')
        #Back = types.InlineKeyboardButton('Back', callback_data='Back')
        #markup_inline.add(Join1, Back)
        #bot.send_message(callback.message.chat.id, "For the quality of the signals provided, we have gathered the best privateers in our team. Our Privateers are professional forecasters and cover a large number of events, carefully analyzing each and giving their own recommendations. This approach brings very good results.", reply_markup=markup_inline)
    elif callback.data == 'INFO4':
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        Join1 = types.InlineKeyboardButton('Join a channel', url='https://paywall.pw/8k6mlzrmqjdo')
        Back = types.InlineKeyboardButton('Back', callback_data='Back')
        markup_inline.add(Join1, Back)
        bot.send_message(callback.message.chat.id, "The best forex robot that is dominating the chart right now. Trading with Dragon Expert's Triangular Pairs Correlation Strategy ensures that you can earn 70%-100%++ Profits Monthly. The most advanced real time algorithm algorithm in EA software. Connect to our channel and download all the necessary files to set up and run the bot.", reply_markup=markup_inline)


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
