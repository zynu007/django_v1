from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def home(request):
    return HttpResponse('Hello this is your home page of the poll website')

def about(request):
    return HttpResponse('This is a test webpage. Thank you.')

def detail(request, question_id):
    
        question = get_object_or_404(Question, pk=question_id)
        return render(request,'polls/detail.html',{'question':question})




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)





def result(request, qstn_id):
    response = 'You are loing at the results of question %s.'
    return HttpResponse(response %qstn_id)

def vote(request, qstn_id):
    return HttpResponse('you are voting on the question %s.' %qstn_id)