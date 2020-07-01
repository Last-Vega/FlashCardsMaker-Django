from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from register.models import Flashcards
from django.db.models import Q
import logging
logger = logging.getLogger('development')
# Create your views here.

def learning_list(request):
    flashcards = Flashcards.objects.only('words')
    #flashcards = Flashcards.objects.filter(name__startwith='query')
    return render(request, 'learning.html', {'flashcards': flashcards})

def check_answer(request):
    answer_words = request.POST.getlist('answer')
    flashcards = Flashcards.objects.all()
    #logger.debug("self.request.POST.get() = " + request.POST.getlist('answer', None)[1])
    temp_list = []
    for i, _ in enumerate(flashcards):
        temp_list.append({
            'flashcards': flashcards[i],
            'answer_words': answer_words[i],
        })
    return render(request, 'check_answer.html', {'temp_list': temp_list,})
