from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question # tb 추가

# Create your views here.

def index(request) :
    question_list = Question.objects.order_by('-create_date') # 날짜의 역순(최신순)으로 조회
    context = {'question_list' : question_list} # .html의 question_list에 값에 대입됨 해당
    return render(request, 'pybo/question_list.html', context) # 요청은 pybo/question_list.html의 템플릿에 담기
                                                                            # config/settins.py 의 templates에 경로 설정하기

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # question_id가 없으면 404에러 리턴
    context = {'question_' : question} # .html question_은 question 값이 대입됨
    return render(request, 'pybo/question_detail.html', context)

