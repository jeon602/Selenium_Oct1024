import requests
from bs4 import BeautifulSoup

# 여러 URL을 리스트로 정의
urls = [
    "https://risebridgegolf.com/",
    "http://woolstonmanor.co.uk/golf/",
    # 다른 골프장 URL 추가 가능
]

# 각 URL을 처리하는 함수 정의
def scrape_golf_club_info(url):
    try:
        # URL 요청
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공했는지 확인

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')

        # 타이틀 추출
        title = soup.find('h2').get_text() if soup.find('h2') else "Title not found"
        print(f"Title: {title}")

        # 주소 추출
        address = soup.find('span', class_='contact-address')
        print(f"Address: {address.get_text() if address else 'Address not found'}")

        # 이메일 추출
        email = soup.find('a', href=lambda href: href and "mailto:" in href)
        email_address = email.get('href').replace('mailto:', '') if email else 'Email not found'
        print(f"Email: {email_address}")

        # 전화번호 추출
        phone = soup.find('span', class_='contact-phone')
        print(f"Phone: {phone.get_text() if phone else 'Phone not found'}")

        # 팩스번호 추출
        fax = soup.find('span', class_='contact-fax')
        print(f"Fax Number: {fax.get_text() if fax else 'Fax Number not found'}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# 여러 URL을 반복 처리
for url in urls:
    print(f"\nScraping URL: {url}")
    scrape_golf_club_info(url)

