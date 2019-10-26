from django.shortcuts import render
from .models import AngelFind
from crawler.crawl import *
import datetime
from django.utils import timezone
from lostpet.models import AngelLost
from django.db.models import Q
from django.core.paginator import Paginator


def crawler(dog_url, cat_url):
    
    # 강아지 보호정보
    lostPet = angel_crawler(dog_url)
    checkoutData = AngelFind.objects.filter(group='dog').last()
    if (checkoutData != None) and (lostPet[-1]['link'] == checkoutData.link):
        pass
    else:
        for pet in lostPet:
            data = AngelFind(where = pet['where'], link = pet['link'], thumb=pet['thumb'], species = pet['species'], date = pet['date'], group='dog')
            data.save()

    # 고양이 보호정보
    lostPet = angel_crawler(cat_url)
    checkoutData = AngelFind.objects.filter(group='cat').last()
    if (checkoutData != None) and (lostPet[-1]['link'] == checkoutData.link):
        pass
    else:
        for pet in lostPet:
            data = AngelFind(where = pet['where'], link = pet['link'], thumb=pet['thumb'], species = pet['species'], date = pet['date'], group='cat')
            data.save()
    
    return AngelFind.objects.all()

def list(request):
    dog_crawling_url = "http://www.angel.or.kr/index.php?listType=&style=webzine&code=dog&ski=&sci=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84&sco=%EC%B2%9C%EC%95%88%EC%8B%9C+%EB%8F%99%EB%82%A8%EA%B5%AC&sgu=K"
    cat_crawling_url = "http://www.angel.or.kr/index.php?listType=&style=webzine&code=cat&ski=&sci=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84&sco=%EC%B2%9C%EC%95%88%EC%8B%9C+%EB%8F%99%EB%82%A8%EA%B5%AC&sgu=K"
    dog_check = AngelFind.objects.filter(group='dog').last()
    cat_check = AngelFind.objects.filter(group='cat').last()
    # 크롤링된 데이터가 있는지 확인
    if (dog_check == None) or (cat_check == None):
        crawler(dog_crawling_url, cat_crawling_url)

        
    current = datetime.datetime.now()
    # 데이터가 없는 경우 크롤링 후 다시 로드
    checkoutData = AngelFind.objects.last()
    time_diff = current - checkoutData.created_at 
    
    # 하루가 지났는지 계산
    if time_diff.seconds > 8640:
        crawler(dog_crawling_url, cat_crawling_url)
    
    
    pet_list = AngelFind.objects.order_by('-date')
    

    # -----------------pagination-------------------------
    
    paginator = Paginator(pet_list, 7)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    
    page_range = []
    # templates 에서 쓰기 위한 페이지 레인지 저장
    for r in range(board.paginator.num_pages):
        page_range.append(int(r + 1))
    
    
    # ----------------여기서부터 검색 기능 -------------------
    linked_pet = []
    word_list = []
    for query in board:
        
        word = query.species.strip().split(' ')
        word_list.append(word)
        
        word = query.where.strip().split(' ')
        word_list.append(word)
        
        searched_list = searcher(word_list)
    
        uni_qs = searched_list[0]
        
        for qs in searched_list:
            uni_qs = uni_qs | qs
        
        linked_pet.append(uni_qs)
        word_list = []
    
    
    # ---------------- 검색된 펫과, 페이지네이션 된 배열을 연결합니다.
    zipped_list = zip(board, linked_pet)
    
    
    return render(request, 'findpetpage.html',{'context':zipped_list, 'board':board, 'page_range': page_range })


def searcher(word):
    # 참고 https://jamanbbo.tistory.com/21
    searched_list = []
    
    for col_key in word:
        for keyword in col_key:
            slist = AngelLost.objects.filter(Q(where__icontains=keyword)|Q(species__icontains=keyword)).distinct()

            searched_list.append(slist)
            
    return searched_list