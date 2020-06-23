from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'retrieval'
urlpatterns = [
    path('retrieval/', views.retrieval_list, name='retrieval_list'),
]
