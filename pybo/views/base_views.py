from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from pybo.models import Question


def index(request):
    page = request.GET.get('page', '1') # 디폴트 페이지는 1로 설정
    kw = request.GET.get('kw', '') # get으로 받은 검색어 값
    question_list = Question.objects.order_by('-create_date')  # 날짜의 역순(최신순)으로 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |                  # 제목 검색
            Q(content__icontains=kw) |                  # 내용 검색
            Q(answer__content__icontains=kw) |          # 답변 내용 검색
            Q(author__username__icontains=kw) |         # 작성자 검색
            Q(answer__author__username__icontains=kw)   # 답변 작성자 검색
        ).distinct()
    paginator = Paginator(question_list, 15) # 페이지당 15개씩 보이기
    page_obj = paginator.get_page(page) # 장고 내부적으로 전체 데이터를 조회하지않고 해당 페이지의 데이터만 조회하는 쿼리
    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    # context = {'question_list': question_list}  # .html의 question_list에 값에 대입됨 해당
    return render(request, 'pybo/question_list.html', context)  # 요청은 pybo/question_list.html의 템플릿에 담기
    # config/settins.py 의 templates에 경로 설정하기


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # question_id가 없으면 404에러 리턴
    context = {'question': question}  # .html question은 question 값이 대입됨
    return render(request, 'pybo/question_detail.html', context)
    