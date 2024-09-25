from django.shortcuts import render ,redirect
from .models import Question,Answers
from .forms import QuestionForm,AnswersForm

# Create your views here.
def questions_list(request):
    data = Question.objects.all()
    return render (request,'ques_list.html',{'questions':data})
def questions_detail(request,pk):
    data = Question.objects.get(id=pk)
    return render(request,'questions_detail.html',{'question':data})