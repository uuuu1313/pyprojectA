from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# DB 생성시 config/settings.py 의 INSTALLES_APPS에 pybo.apps의 메서드 추가 해주기
class Question(models.Model): # Question Tb 생성
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model): # Answer Tb 생성
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키의 값이 삭제되면 같이 삭제되는 필드
    content = models.TextField()
    create_date = models.DateTimeField()

