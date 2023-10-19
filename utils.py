import openai
import requests
import bs4
from options import country_newspapers

def create_prompt():
    country = input("What country are you interested in for news? ")
    try:
        url, tag = country_newspapers[country]
    except:
        print("Sorry, country not supported")
        return
    
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    country_headlines = ""
    available_headlines = soup.select(tag)[:3]
    for item in available_headlines:
        country_headlines += f"{item.get_text()}\n"
    
    prompt = "Detect the language of the news headlines below then translate a summary of the headlines to English in a conversational tone.\n"
    return prompt + country_headlines

def openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.1,
        top_p=1.0
    )
    return response['choices'][0]['text']