from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'learning'
urlpatterns = [
    path('learning/', views.learning_list, name='learning_list'),
    path('learning/check_answer', views.check_answer, name='check_answer'),

]
