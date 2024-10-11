import requests
from bs4 import BeautifulSoup

url = "https://risebridgegolf.com/"
resqonse = requests.get(url)

soup =BeautifulSoup(resqonse.text, 'html.parser')

title =soup.find('h2').get_text()
print(title)

# h2 태그에 해당하는 내용 스크랩 성공