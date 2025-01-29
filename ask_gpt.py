from openai import OpenAI
import json
import sqlite3
import os
from time import time
import colorama
from alive_progress import alive_bar

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

print(colorama.Fore.GREEN + "Database created and populated")

def run_query(query):
    cur.execute(query)
    return cur.fetchall()

# OPENAI
configPath = getPath("auth.json")
with open(configPath, "r") as f:
    config = json.load(f)

openai = OpenAI(api_key=config["openaiKey"])

def ask_gpt(content):
    stream = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    response_list = []
    buffer = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            buffer += chunk.choices[0].delta.content
            if '\n' in buffer:
                lines = buffer.split('\n')
                for line in lines[:-1]:
                    print(line.strip())
                    response_list.append(line + '\n')
                buffer = lines[-1]

    if buffer:
        print(buffer.strip())
        response_list.append(buffer)

    print()  # New line after the response
    return "".join(response_list)


# Strategies to get a correct answer
with open(createTablePath, "r") as f:
    schema = f.read()

common_sql_request = "Give me a SQLite SELECT statement that answers the question. Only respond with SQLite syntax. If there is an error, do not explain it!"

strategies = {
    "zero_shot": schema + common_sql_request,
    "single_domain_example": (schema + 
                              " Which users have more than one game in their inventory? " + 
                              " \nSELECT u.userID, u.username, COUNT(ui.gameID) as game_count\nFROM Users u\nJOIN UserInventory ui ON u.userID = ui.userID\nGROUP BY u.userID\nHAVING game_count > 1;\n " +
                              common_sql_request)
}

questions = [
    "Which are the most expensive games?",
    "Which users have participated in the most trades?",
    "What are the top 3 most common game genres?",
    "Which games are included in bundles with a discount greater than 15%?",
    "Who are the users that have both offered and received games in trades?",
    "What is the average base price of games for each platform?",
    "Which users have games in their inventory but haven't made any trades?",
    "What is the total value of each user's inventory based on the current trade values?",
    "Who has referred who in the referral program?",
]

def sanitize_for_just_sql(value):
    gpt_start_sql_marker = "```"
    gpt_end_sql_marker = "```"
    if gpt_start_sql_marker in value:
        value = value.split(gpt_start_sql_marker)[1]
    if gpt_end_sql_marker in value:
        value = value.split(gpt_end_sql_marker)[0]
    return value.strip()

for strategy in strategies:
    responses = {"strategy": strategy, "prompt_prefix": strategies[strategy]}
    question_results = []
    
    print(colorama.Fore.YELLOW + f"\nUsing strategy: {strategy}")
    with alive_bar(len(questions), title="Processing Questions", bar="classic2", spinner="dots_waves") as bar:
        for question in questions:
            print(colorama.Fore.CYAN + f"\nQuestion: {question}")
            error = "None"
            try:
                print(colorama.Fore.YELLOW + "Generating SQL Query...")
                sql_syntax_response = ask_gpt(strategies[strategy] + " " + question)
                sql_syntax_response = sanitize_for_just_sql(sql_syntax_response)
                print(colorama.Fore.MAGENTA + "SQL Query:")
                print(sql_syntax_response)

                print(colorama.Fore.YELLOW + "Executing Query...")
                query_raw_response = str(run_query(sql_syntax_response))
                print(colorama.Fore.BLUE + "Raw Query Result:")
                print(query_raw_response)

                print(colorama.Fore.YELLOW + "Generating Friendly Response...")
                friendly_results_prompt = f"I asked a question '{question}' and the response was '{query_raw_response}'. Please give a concise response in a more friendly way. Do not give any other suggestions or chatter."
                friendly_response = ask_gpt(friendly_results_prompt)
                print(colorama.Fore.GREEN + "Friendly Response:")
                print(friendly_response)
                
            except Exception as err:
                error = str(err)
                print(colorama.Fore.RED + f"Error: {error}")

            question_results.append({
                "question": question,
                "sql": sql_syntax_response,
                "queryRawResponse": query_raw_response,
                "friendlyResponse": friendly_response,
                "error": error
            })
            bar()

    responses["questionResults"] = question_results

    with open(getPath(f"response_{strategy}_{time()}.json"), "w") as outFile:
        json.dump(responses, outFile, indent=2)

cur.close()
conn.close()
print(colorama.Fore.GREEN + "Done!")
