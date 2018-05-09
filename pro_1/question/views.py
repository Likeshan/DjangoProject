from django.shortcuts import render
from django.http import HttpResponse
from question.models import *	
# Create your views here.
def index(request):
	#return HttpResponse('hello world')
	#contex = {'message':'this is a ABC'}
	person_list = Person.objects.all()
	contex = {'person_list':person_list}
	return render(request,'question/index.html',contex)