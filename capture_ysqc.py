import requests
from bs4 import BeautifulSoup

def capture_chapter_list():
    url = "https://www.gxwztv.com/128/128143/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    capture = soup.select("#chapters-list")[0].select('li')[200:300]
    chapters_list = []
    for chapter in capture:
        chapters_list.append(("https://www.gxwztv.com" + chapter.select("a")[0]["href"], chapter.select("a")[0].text))
    return chapters_list


def capture_content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.select("#txtContent")[0].get_text('\n', 'br/')
    return content

