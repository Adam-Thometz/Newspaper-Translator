import openai
from secret import OPENAI_API_KEY
from utils import create_prompt, openai_response

openai.api_key = OPENAI_API_KEY

headlines = create_prompt()
print(headlines)

response = openai_response(headlines=headlines)
print(response)