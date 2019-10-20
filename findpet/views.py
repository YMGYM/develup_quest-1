from django.shortcuts import render
from .models import AngelFind
from crawler.crawl import *
import datetime
from django.utils import timezone


def crawler(url):
    lostPet = angel_crawler(url)
    checkoutData = AngelFind.objects.last()
    
    if (checkoutData != None) and (lostPet[-1]['link'] == checkoutData.link):
        pass
    else:
        for pet in lostPet:
            data = AngelFind(where = pet['where'], link = pet['link'], thumb=pet['thumb'], species = pet['species'], date = pet['date'], group='dog')
            data.save()

    
    return AngelFind.objects.all()

def list(request):
    crawling_url = "http://www.angel.or.kr/index.php?listType=&style=webzine&code=dog&ski=&sci=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84&sco=%EC%B2%9C%EC%95%88%EC%8B%9C+%EB%8F%99%EB%82%A8%EA%B5%AC&sgu=L"
    checkoutData = AngelFind.objects.last()
    
    # 크롤링된 데이터가 있는지 확인
    if checkoutData == None:
        pet_list = crawler(crawling_url)

        
    current = datetime.datetime.now()
    # 데이터가 없는 경우 크롤링 후 다시 로드
    checkoutData = AngelFind.objects.last()
    time_diff = current - checkoutData.created_at 
    
    # 하루가 지났는지 계산
    if time_diff.seconds > 8640:
        pet_list = crawler(crawling_url)
    
    
    pet_list = AngelFind.objects.all()
    

    return render(request, 'findpetpage.html',{'pet_list':pet_list})