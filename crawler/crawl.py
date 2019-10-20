from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# 참고 https://www.fun-coding.org/DS&AL3-4.html
# 참고 https://webnautes.tistory.com/779


def angel_crawler(angel_url):
    # html = urlopen("http://www.angel.or.kr/index.php?listType=&style=webzine&code=dog&ski=&sci=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84&sco=%EC%B2%9C%EC%95%88%EC%8B%9C+%EB%8F%99%EB%82%A8%EA%B5%AC&sgu=L")
    html = urlopen(angel_url)
    bsObject = BeautifulSoup(html, "html.parser")

    parsed_object = bsObject.body.find_all("ul", {'class' : 'reportlist'})

    lostPet = []
    for i in parsed_object:
        pet_dict = {}

        # 실종 장소 파싱
        pet_dict['where'] = i.find('li', {'class': 'reportlist_detail'}).find('span', {'class':'title'}).find('a').text


        # 링크 파싱
        pet_dict['link'] = "http://www.angel.or.kr/" + i.find('li', {'class': 'reportlist_detail'}).find('span', {'class':'title'}).find('a').get('href')


        # 썸네일 파싱
        # 주소가 이상해도 썸네일이 파싱되기 때문에 그대로 두겠습니다.
        pet_dict['thumb'] = "http://www.angel.or.kr/" + i.find('li', {'class': 'reportlist_photo'}).find('div', {'class':'webzinethumb'}).find('a').find('img').get('src')


        # # 상세설명 파싱(미완성)
        # parse = i.find('li', {'class': 'reportlist_detail'})
        # parse = str(parse)

        # filt = re.compile('(<[^/]+</[A-Za-z]+>)')
        # aa = filt.sub('',parse)
        # pet_dict['detail'] = aa

        # print(pet_dict['detail'])

        # 종 파싱
        pet_dict['species'] = i.find('li', {'class': 'reportlist_breeds'}).find('a').text

        # 날짜 파싱
        pet_dict['date'] = i.find('li', {'class': 'reportlist_date'}).text


        # 완성된 딕셔너리를 리스트에 추가
        lostPet.append(pet_dict)

    return lostPet