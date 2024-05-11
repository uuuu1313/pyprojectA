from django.urls import path

from pybo import views

app_name = 'pybo' # 다른 앱과 구분될 수 있게 앱네임 사용

urlpatterns = [
    path('', views.index, name='index'), # pybo/ url은 pybo.views의 index 함수에 정의함
    path('<int:question_id>/', views.detail, name='detail'), # question 게시글 상세 보기는 views의 detail함수에 정의
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>', views.answer_delete, name='answer_delete')
]