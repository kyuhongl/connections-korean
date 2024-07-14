import requests
from bs4 import BeautifulSoup
from translate import translate_to_korean

def scrape_page():

    url = 'https://www.digitaltrends.com/gaming/nyt-connections-today-answer-hints-july-14/' # although this website is a static url, it links to the latest answers
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    answers = soup.find(attrs={'data-testid': 'solved-category-container'}).get_text().strip().split("\n")
        
    categories = []
    individual_words = []
    for i in range(0, len(answers)):
        try:
            temp1, temp2 = answers[i].split("-") # i've noticed that occasionally the website uses different types of hyphens, colons, etc. so i've added some exceptions
        except: 
            try:
                temp1, temp2 = answers[i].split("–") 
            except:
                temp1, temp2 = answers[i].split(":")
        temp1 = translate_to_korean(temp1)
        temp2 = translate_to_korean(temp2)
        categories.append(temp1)
        individual_words.append(temp2.split(", "))
    return categories, individual_words
    # except Exception as e:
    #     print("Error in SCRAPING", e)
    #     return None, None
