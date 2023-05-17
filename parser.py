import logging
import random
from typing import List

import praw
from prawcore import ResponseException
from telebot.types import InputMediaPhoto

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RedditParser:
    def __init__(
        self,
        reddit_clientid: str,
        reddit_secret: str,
        subs_list: List[str]
    ):
        self.reddit = praw.Reddit(
            client_id=reddit_clientid,
            client_secret=reddit_secret,
            user_agent="/r/pics grabber v1.0"
        )
        try:
            self.reddit.user.me()
        except ResponseException as e:
            logger.exception(e)
        self.subs_list = subs_list

    def get_image_links_from_reddit(self):
        try:
            subreddit = self.reddit.subreddit(random.choice(self.subs_list))
            posts = subreddit.hot()
            img_list = []
            for post in posts:
                if post.url.endswith(('jpg', 'jpeg', 'png')):
                    img_list.append(post)

            res = [
                InputMediaPhoto(x.url) for x in random.choices(img_list, k=2)
            ]
            return res
        except Exception as e:
            logger.exception(e)
