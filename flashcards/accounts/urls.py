from django.conf.urls import url, include
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_account, name='create_account'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),

]
