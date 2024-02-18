import logging

import telebot

from config import TOKEN, CHAT_IDS
from web_parser import RandomImage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    bot = telebot.TeleBot(TOKEN)
    image = RandomImage()
    try:
        for chat_id in CHAT_IDS:
            bot.send_photo(chat_id=chat_id, photo=image)
    except Exception as e:
        logger.error(e)
        # if CHAT_IDS is 1 chat_id
        bot.send_photo(chat_id=CHAT_IDS[0], photo=image)


if __name__ == "__main__":
    main()
