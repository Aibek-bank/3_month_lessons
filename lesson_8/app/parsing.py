from bs4 import BeautifulSoup
import requests

def get_news():
    url = 'https://24.kg'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_news = soup.find_all("div", class_="title")[:20]
    news_list = []

    for news in all_news:
        title = news.text.strip()
        link = news.find("a")['href'] if news.find("a") else url
        full_link = link if link.startswith("http") else f"https://24.kg"
        news_list.append(f"{title}\n{full_link}")

    return news_list