# session_manager.py
from telethon import TelegramClient
from config import API_ID, API_HASH

def create_client(session_name):
    client = TelegramClient(session_name, API_ID, API_HASH)
    return client
