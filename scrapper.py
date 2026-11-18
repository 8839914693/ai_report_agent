import requests
from bs4 import BeautifulSoup   

def scrap_website(url):
    articles  = []
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.find_all('article'):
            title = article.find('h2').get_text(strip=True)
            link = article.find('a')['href']
            date = article.find('time')['datetime']
            articles.append({'title': title, 'link': link, 'date': date })
        return articles
    except Exception as e:
        print(f"An error occurred while trying to scrape the website: {e}")
        return None