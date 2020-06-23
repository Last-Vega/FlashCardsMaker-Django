from django.forms import ModelForm
from register.models import Flashcards

class FlashcardsForm(ModelForm):
    """単語帳フォーム"""
    class Meta:
        model = Flashcards
        fields = ('words', 'meanings', 'part_of_speech', 'synonym', 'sentence', )
        
