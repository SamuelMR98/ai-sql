# ai-sql

This lab is part of the CS452 - Database Modeling Concepts course. The description of the lab can be found [here](description.md).

## Video game trading-store database

### Description

This database represents the mockup of a video game trading-store where users can trade games with each other and buy game bundles at a discounted price.

More details about the database can be found [here](database.md).

### How to run

ask_gpt.py is a Python script that uses the OpenAI GPT-4 API to generate SQL queries based on user input. To run the script, you need to have an OpenAI API key. You can get one by signing up [here](https://beta.openai.com/signup/).

Once you have the API key, you can run the script as follows:

The auth data should be stored in a file called `auth.json` in the following format:

```json
{
    "openaiKey": "your_api_key"
    "orgId" : "your_org_id"
}
```

Then, you can run the script as follows:

```bash
python ask_gpt.py
```

The script will prompt you to enter a question. Based on your input, it will generate a SQL query using the OpenAI GPT-4 API.
