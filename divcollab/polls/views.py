from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Polls Index.")

def detail(request, question_id):
	return HttpResponse("Question: %s." % question_id)

def results(request, question_id):
	response = "Results for question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Enter vote for question %s." % question_id)
