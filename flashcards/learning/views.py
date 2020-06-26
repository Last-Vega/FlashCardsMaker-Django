from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from register.models import Flashcards
from django.db.models import Q
# Create your views here.

def learning_list(request):
    flashcards = Flashcards.objects.only('words')
    #flashcards = Flashcards.objects.filter(name__startwith='query')
    return render(request, 'learning.html', {'flashcards': flashcards})

def check_answer(request):
    answer_words = request.POST.get('answer')
    return render(request, 'check_answer.html', {'answer_words': answer_words})
