from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index), # pybo/ url은 pybo.views의 index 함수에 정의함
]