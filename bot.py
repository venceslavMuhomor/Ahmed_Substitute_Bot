import logging
from urllib.parse import urlsplit

import telebot

from config import TOKEN, CHAT_IDS
from parser import get_image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    bot = telebot.TeleBot(TOKEN, parse_mode=None)
    image = get_image()
    image_type = urlsplit(image).path.split('.')[-1]

    if image_type in ['png', 'jpeg', 'jpg']:
        for chat_id in CHAT_IDS:
            bot.send_photo(chat_id, image)
            logger.info("Bot sends image to chat id: %s" % chat_id)
    else:
        for chat_id in CHAT_IDS:
            bot.send_message(chat_id, image)
            logger.warning("file type not correct, use parser from new resource")
            logger.info("Bot sends url to chat id: %s" % chat_id)


if __name__ == "__main__":
    main()
