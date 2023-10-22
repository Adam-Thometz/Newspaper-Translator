import openai
import requests
import bs4
from options import country_newspapers

def create_prompt():
    country = input("What country are you interested in for news? ")
    try:
        url = country_newspapers[country]
    except:
        print("Sorry, country not supported")
        return
    
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    country_headlines = ""
    available_headlines = soup.find_all("h2")[:10]
    for item in available_headlines:
        country_headlines += f"{item.get_text()}\n"
    
    return country_headlines

def openai_response(headlines):
    messages = [
        {"role": "system", "content": "You take a list of news headlines in foreign languages then extract the three most prominent topics in English."},
        {"role": "user", "content": headlines}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.7,
        top_p=1.0
    )
    return response['choices'][0]['message']['content']