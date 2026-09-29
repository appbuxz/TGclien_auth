import asyncio, dotenv, os, asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH

client = TelegramClient(
    "test",
    API_ID,
    API_HASH
)


client.start()

print("Client Connected")

client.disconnect()
