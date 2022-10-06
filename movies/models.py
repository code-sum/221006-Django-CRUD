from django.db import models

# Create your models here.

'''
영화 목록 리스트
- 영화 제목 (title)
- 영화 줄거리 (summary)
- 영화 상영 시간 (running_time)
'''

class Movie(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time = models.IntegerField()