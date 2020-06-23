from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from register.models import Flashcards
from django.db.models import Q
# Create your views here.

def retrieval_list(request):
    query_word = request.GET.get("query")
    if query_word:
        flashcards = Flashcards.objects.filter(words__startswith=query_word)
    else:
        flashcards = Flashcards.objects.all()
    #flashcards = Flashcards.objects.filter(name__startwith='query')
    return render(request, 'retrieval.html', {'flashcards': flashcards})
