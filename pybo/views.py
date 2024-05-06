from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import Question  # tb 추가
from .forms import QuestionForm, AnswerForm  # 검증


# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')  # 날짜의 역순(최신순)으로 조회
    context = {'question_list': question_list}  # .html의 question_list에 값에 대입됨 해당
    return render(request, 'pybo/question_list.html', context)  # 요청은 pybo/question_list.html의 템플릿에 담기
    # config/settins.py 의 templates에 경로 설정하기


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # question_id가 없으면 404에러 리턴
    context = {'question': question}  # .html question은 question 값이 대입됨
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # # Question과 Answer는 ForeignKey로 연결되어 question에서 answer를 참조 가능 (question.answer_set.create~)
    # # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now()) #위와 동일
    # # 위 코드를 사용시 answer.save() 세이브를 해야함

    # 답변 등록 시
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # request.POST 에는 입력안 값이 저장됨
        if form.is_valid():  # 폼이 유효할 때
            question = form.save(commit=False)  # commit=False는 임시 저장의 뜻, question 객체를 리턴함
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
