from bs4 import BeautifulSoup
import requests, time

count_news = 0

with open("news.txt", "w", encoding='utf-16') as file:
    for page in range(1, 500):
        url = f"https://24.kg/page_{page}"
        response = requests.get(url=url)
        print(response)
        soup = BeautifulSoup(response.text, "lxml")

        all_news = soup.find_all("div", class_='title')
        print(all_news)

        for news in all_news:
            count_news += 1
            file.write(f'{count_news} {news.text}\n')
            print(count_news, news.text)
