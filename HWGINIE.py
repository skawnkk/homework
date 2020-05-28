import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#tr불러오기
trs=soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for tr in trs:
    title=tr.select_one('td.info > a.title.ellipsis')
    name=title.text.strip()
    ranking=tr.select_one('td.number').text.split()[0]
    singer=tr.select_one('td.info > a.artist.ellipsis').text
    print(ranking, name, singer)

 
# for tr in trs:
#     title=tr.select_one('td.title > div > a')
#     if title is not None:
#         movie=title.text 
#         ranking=tr.select_one('td:nth-child(1) > img')['alt']
#         star=tr.select_one('td.point').text
       
#         print(ranking, movie, star)
#     #     # movie=title.text
#     #     number=tr.select_one('td:nth-child(1) > img')
#     #     print(number)

#     # # test=tr.select_one('td.point')
#     # # print(test)