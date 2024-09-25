from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='ques_user')
    question =models.CharField(max_length=100)
    content =models.TextField(max_length=500)
    create_date=models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
class Answers(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='answer_user')
    answer = models.TextField(max_length=500)
    question = models.ForeignKey(Question,related_name='answer_ques',on_delete=models.CASCADE)
    create_date=models.DateTimeField(default=timezone.now)