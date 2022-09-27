import os

env = os.environ


reddit_clientid = env.get('reddit_clientid')
reddit_secret = env.get('reddit_secret')
subs_list = list(env.get('subs_list').split(','))
TOKEN = env.get("TOKEN")
CHAT_IDS = tuple(env.get("CHAT_IDS").split(","))
