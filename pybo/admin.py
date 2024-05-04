from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 'subject' 컬럼으로 관리자 화면에 검색 기능추가

admin.site.register(Question, QuestionAdmin) # 관리자 화면에서 Question 테이블을 관리하기