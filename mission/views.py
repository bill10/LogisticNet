from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.user.profile.name
    job = request.user.profile.get_jobs()
    company = request.user.profile.company
    return HttpResponse("Hello, {} {} from {}".format(job,name,company))