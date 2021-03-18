import requests
from bs4 import BeautifulSoup


def crawlingTest():
    # HTTP GET Request
    req = requests.get('https://ridibooks.com/category/books/3001')
    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')

    selects = soup.select('div.book_macro_110 > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)')

    for select in selects:
        print(select.get('href'))