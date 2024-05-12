from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from pybo.forms import QuestionForm
from pybo.models import Question


@login_required(login_url='common:login') # 자바의 어노테이션과 동일, 미로그인시 urls의 common:login 경로로 이동시킴
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # request.POST 에는 입력안 값이 저장됨
        if form.is_valid():  # 폼이 유효할 때
            question = form.save(commit=False)  # commit=False는 임시 저장의 뜻, question 객체를 리턴함
            question.author = request.user # request.user는 현재 로그인한 계정의 User 모델 객체
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다#')
        return redirect('pybo:detail', question_id=question.id) # 로그인한 유저와 작성자 유저가 일치 않을시 pybo/question_id로 이동
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question) # instance 값을 지정하면 폼 속성값이 instance 값으로 채워짐, reuqest.POST의 값으로 덮어쓰기
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question) # form의 속성을 question으로 값으로 채워넣기
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "삭제 권한이 없습니다 #")
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user in question.voter.all():
        question.voter.remove(request.user)
    else:
        if request.user == question.author:
            messages.error(request,"본인의 글은 추천할 수 없습니다 !#")
        else:
            question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)