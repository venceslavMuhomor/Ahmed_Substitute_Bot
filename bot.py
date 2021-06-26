import logging

import telebot

from config import TOKEN, CHAT_IDS
from parser import get_image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    bot = telebot.TeleBot(TOKEN, parse_mode=None)
    image = get_image()
    for chat_id in CHAT_IDS:
        bot.send_photo(chat_id, image)
        logger.info("Bot sends image to chat id: %s" % chat_id)


if __name__ == "__main__":
    main()
