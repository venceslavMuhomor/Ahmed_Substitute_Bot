import logging
import random
from typing import List

import praw
from telebot.types import InputMediaPhoto

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RedditParser:
    def __init__(
        self,
        reddit_username: str,
        reddit_password: str,
        reddit_clientid: str,
        reddit_secret: str,
        subs_list: List[str]
    ):
        self.reddit = praw.Reddit(
            username=reddit_username,
            password=reddit_password,
            client_id=reddit_clientid,
            client_secret=reddit_secret,
            user_agent="/r/pics grabber v1.0"
        )
        self.subs_list = subs_list

    def get_image_links_from_reddit(self):
        try:
            subreddit = self.reddit.subreddit(random.choice(self.subs_list))
            posts = subreddit.hot()
            images_list = []
            for post in posts:
                if post.url.endswith(('jpg', 'jpeg', 'png')):
                    images_list.append(post)
            return [InputMediaPhoto(x.url) for x in images_list[:5]]
        except Exception as e:
            logger.exception(e)
