import os
import telebot
from parser import return_joy
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# список груп 1 pyFlood, 2 maevka, 3 ahmed's group
CHATS = os.getenv('CHATS').split(',')

# получаем фотку
try:
    image = return_joy()
except OSError:
    print('сайт не робит')

try:
    for chat in CHATS:
        bot.send_photo(chat, image)
except NameError:
    print('image is not defined')
