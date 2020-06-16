from django.db import models

# Create your models here.

class Flashcards(models.Model):
    """flashcards"""
    words = models.CharField('単語', max_length=255)
    meanings = models.CharField('意味', max_length=255)
    part_of_speech = models.CharField('品詞', max_length=255)
    synonym = models.CharField('類義語', max_length=255)
    sentence = models.CharField('例文', max_length=255)


    def __str__(self):
        return self.words

"""
<td>
<a href="{% url 'cms:book_mod' book_id=book.id %}" class="btn btn-outline-primary btn-sm">修正</a>
<a href="{% url 'cms:book_del' book_id=book.id %}" class="btn btn-outline-danger btn-sm">削除</a>
</td>
"""
