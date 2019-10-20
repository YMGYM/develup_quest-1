from django.db import models

# Create your models here.
class AngelFind(models.Model):
    where = models.CharField(max_length=200)
    link = models.URLField()
    thumb = models.URLField()
    species = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    # 강아지인지 고양이인지
    group = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # 저장 시간을 한국 시간으로 저장하는 코드 
    # 참고 : https://jupiny.com/2016/10/05/model-datetimefield-in-korean/
    