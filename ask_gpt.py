from openai import OpenAI
import json
import sqlite3
import os
from time import time
import colorama
import alive_progress

colorama.init()

# Start message
print(colorama.Fore.GREEN + "Running ask_gpt.py")
print(colorama.Fore.GREEN + "This script will ask the GPT-3 model for a sql response to a question.")

# Load the API key
with open("config.json") as f:
    config = json.load(f)
    api_key = config

# SQLITE database setup
sqliteDb = "data.db"