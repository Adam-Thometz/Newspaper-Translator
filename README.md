# Newspaper Trnaslator

This is a web scraping app that gets headlines from foreign newspapers and translates them into English using AI.

## Tech used
- Python
- OpenAI API
- Beautiful Soup + LXML

## Setup (from root directory)
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install`
4. `touch secret.py`
5. `echo "OPENAI_API_KEY = <your OpenAI API key>"`

Run with `python3 main.py`.