# main.py
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")

print(f"API Key: {api_key}")
