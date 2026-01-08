import json
import requests
import os
from dotenv import load_dotenv


# main.py

# take environment variables from .env.
load_dotenv() 

api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")

print(f"API Key: {api_key}")


