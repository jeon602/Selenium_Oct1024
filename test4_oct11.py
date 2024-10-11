# 여러 개의 골프장 이메일, 전화 번호, 팩스번호, 주소 추출
#

import requests
from bs4 import BeautifulSoup
import mysql.connector

# MariaDB 연결 정보 설정
db_connection = mysql.connector.connect(
    host="localhost",       # MariaDB 호스트 주소
    user="",       # MariaDB 사용자 이름
    password="", # MariaDB 비밀번호
    database="golf_db"      # 사용할 데이터베이스 이름
)

cursor = db_connection.cursor()

# 여러 URL 정의
urls = [
    "https://risebridgegolf.com/",
    "http://woolstonmanor.co.uk/golf/",
    # 더 많은 URL 추가 가능
]

# 데이터 삽입 함수
def save_to_db(name, address, email, phone, fax):
    sql = "INSERT INTO golf_club (name, address, email, phone, fax) VALUES (%s, %s, %s, %s, %s)"
    val = (name, address, email, phone, fax)
    cursor.execute(sql, val)
    db_connection.commit()

# 웹 스크래핑 함수
def scrape_golf_club_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 타이틀 (골프장 이름)
    name = soup.find('h2').get_text() if soup.find('h2') else "Name not found"

    # 주소 추출 (HTML 구조에 따라 수정 필요)
    address = soup.find('span', class_='contact-address').get_text() if soup.find('span', class_='contact-address') else "Address not found"

    # 이메일 추출 (mailto 링크)
    email_tag = soup.find('a', href=lambda href: href and "mailto:" in href)
    email = email_tag.get('href').replace('mailto:', '') if email_tag else "Email not found"

    # 전화번호 추출
    phone = soup.find('span', class_='contact-phone').get_text() if soup.find('span', class_='contact-phone') else "Phone not found"

    # 팩스번호 추출
    fax = soup.find('span', class_='contact-fax').get_text() if soup.find('span', class_='contact-fax') else "Fax not found"

    # DB에 저장
    save_to_db(name, address, email, phone, fax)

# URL마다 데이터 처리
for url in urls:
    print(f"Scraping data from: {url}")
    scrape_golf_club_info(url)

# DB 연결 종료
cursor.close()
db_connection.close()
