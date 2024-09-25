from django import forms
from .models import Question,Answers

class QuestionForm(forms.ModelForm):
    class meta :
        model = Question
        exclude = ('author',)
class AnswersForm(forms.ModelForm):
    class meta :
        model = Answers
        fields =['answer']