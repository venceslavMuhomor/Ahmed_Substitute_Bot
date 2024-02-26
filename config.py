
from decouple import config

TOKEN = config('TOKEN')
CHAT_IDS = tuple(config('CHAT_IDS').split(','))
URL = config('URL')