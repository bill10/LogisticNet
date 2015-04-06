from django.shortcuts import render
from django.http import HttpResponse


def login(request, company_name_slug):
    return HttpResponse("Hello {}!".format(company_name_slug))