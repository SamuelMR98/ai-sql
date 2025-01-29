from openai import OpenAI
import json
import sqlite3
import os
from time import time
import colorama
import alive_progress

colorama.init()

print(colorama.Fore.GREEN + "Running ask_gpt.py")


client = OpenAI(
  api_key=""
  )

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);