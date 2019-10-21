from django.db import models


class AngelLost(models.Model):
    where = models.CharField(max_length=200)
    link = models.URLField()
    thumb = models.URLField()
    species = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    # 강아지인지 고양이인지
    group = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)