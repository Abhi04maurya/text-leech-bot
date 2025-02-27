import os

API_ID    = os.environ.get("API_ID", "3670291")
API_HASH  = os.environ.get("API_HASH", "1f55b2e9d972c3a5ac3f008c51ed7a4a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
