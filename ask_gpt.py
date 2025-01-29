from openai import OpenAI
import json
import sqlite3
import os
from time import time
import colorama
import alive_progress

colorama.init()

print(colorama.Fore.GREEN + "Running ask_gpt.py")

# Load and get DB
fdir = os.path.dirname(__file__)
def getPath(filename):
    return os.path.join(fdir, filename)

dbPath = getPath("vgs.db")
createTablePath = getPath("create_tables.sql")
mockDataPath = getPath("mock_data.sql")

# Clean up the DB
if os.path.exists(dbPath):
    os.remove(dbPath)

# Connect to the DB
conn = sqlite3.connect(dbPath)
cur = conn.cursor()

# Create the tables
with open(createTablePath, "r") as f:
    cur.executescript(f.read())

# Insert the mock data
with open(mockDataPath, "r") as f:
    cur.executescript(f.read())

def run_query(query):
    cur.execute(query)
    return cur.fetchall()

# OPENAI
configPath = getPath("auth.json")
with open(configPath, "r") as f:
    config = json.load(f)

openai = OpenAI(config["openaiKey"])



