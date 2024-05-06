from django.urls import path

from pybo import views

app_name = 'pybo' # 다른 앱과 구분될 수 있게 앱네임 사용

urlpatterns = [
    path('', views.index, name='index'), # pybo/ url은 pybo.views의 index 함수에 정의함
    path('<int:question_id>/', views.detail, name='detail'), # question 게시글 상세 보기는 views의 detail함수에 정의
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create')
]