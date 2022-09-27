import logging

import telebot

from config import TOKEN, CHAT_IDS, reddit_clientid, reddit_secret, subs_list

from parser import RedditParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    bot = telebot.TeleBot(TOKEN, parse_mode=None)
    reddit_parser = RedditParser(
        reddit_clientid=reddit_clientid,
        reddit_secret=reddit_secret,
        subs_list=subs_list
    )
    images = reddit_parser.get_image_links_from_reddit()
    for chat_id in CHAT_IDS:
        bot.send_media_group(chat_id=chat_id, media=images)


if __name__ == "__main__":
    main()
