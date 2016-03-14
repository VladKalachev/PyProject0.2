from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

# Create your views here.
import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return HttpResponse("Hove a you?")


def current_datetime(request):
    name = "Vlad"
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now, 'name': name}))
    return HttpResponse(html)