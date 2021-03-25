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

def crawlingRidiBook(bookId):
    headers = [
        {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    ]

    url = 'https://ridibooks.com/books/' + str(bookId)
    htmlText = requests.get(url, headers=headers[0]).text
    soup = BeautifulSoup(htmlText, 'html.parser')
    # selects = soup.select('div.detail_wrap div.detail_body_wrap section.detail_body article.detail_header.trackable')


    isSeries = False if soup.select_one('p.metadata.metadata_info_series_complete_wrap') == None else True
    # print(soup)
    if isSeries == False:
        bookInfo = {
            'title' : soup.select_one('h3.info_title_wrap').text,
            'author' : soup.select_one('a.author_detail_link').text,
            'publisher' : soup.select_one('a.publisher_detail_link').text,
            'ISBN' : soup.select_one('li.isbn_info.Header_Metadata_Detail_Item').text,
            'price': {

            }
        }
        print(bookInfo)

        priceTable = soup.select('table.price_table.normal_price_table tr')

    else:
        print('시리즈 = 무시 ㅇㅋ?')
    # prices = {}

    # print(bookInfo)
    # for priceElement in priceTable:
    #     prices{}
