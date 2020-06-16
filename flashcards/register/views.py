from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from register.models import Flashcards
from register.forms import FlashcardsForm
# Create your views here.


def word_list(request):
    flashcards = Flashcards.objects.all()
    return render(request, 'regist.html', {'flashcards': flashcards})

def flashcards_edit(request, word_id=None):
    """単語の編集"""
    # return HttpResponse('書籍の編集')
    if word_id:   # book_id が指定されている (修正時)
        flashcards = get_object_or_404(Flashcards, pk=word_id)
    else:   # book_id が指定されていない (追加時)
        flashcards = Flashcards()

    if request.method == 'POST':
        form = FlashcardsForm(request.POST, instance=flashcards)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            flashcards = form.save(commit=False)
            flashcards.save()
            return redirect('register:word_list')
    else:    # GET の時
        form = FlashcardsForm(instance=flashcards)  # book インスタンスからフォームを作成

    return render(request, 'edit.html', dict(form=form, word_id=word_id))


def flashcards_del(request, word_id):
    """単語の削除"""
    # return HttpResponse('書籍の削除')
    flashcards = get_object_or_404(Flashcards, pk=word_id)
    flashcards.delete()
    return redirect('register:word_list')
