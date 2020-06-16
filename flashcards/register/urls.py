from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'register'
urlpatterns = [
    path('regist/', views.word_list, name='word_list'),
    path('regist/add/', views.flashcards_edit, name='word_add'),  # 登録
    path('regist/mod/<int:word_id>/', views.flashcards_edit, name='word_mod'),  # 修正
    path('regist/del/<int:word_id>/', views.flashcards_del, name='word_del'),   # 削除
]
