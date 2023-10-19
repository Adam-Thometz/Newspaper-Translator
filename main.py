import openai
from secret import OPENAI_API_KEY
from utils import create_prompt, openai_response

openai.api_key = OPENAI_API_KEY

prompt = create_prompt()
response = openai_response(prompt=prompt)

print(response)
