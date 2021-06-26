import os

env = os.environ

TOKEN = env.get("TOKEN")

CHAT_IDS = tuple(env.get("CHAT_IDS").split(","))
