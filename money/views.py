# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import datetime, date, time

def money(request):
    side_content = 100
    header_name = "Бабки"
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'side_content': side_content,
        'header_name': header_name, 
    })
    return HttpResponse(template.render(context))


def index(request):
    side_content = 100
    header_name = "Главная"
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'side_content': side_content, 
        'header_name': header_name, 
    })
    return HttpResponse(template.render(context))

def indexjq(request):
    header_name = "Главная"
    money = '100грн.'
    dates =date.today()
    time = datetime.now().time
    template = loader.get_template('index-jq.html')
    context = RequestContext(request, {
        'header_name': header_name, 
        'money': money, 
        'date': dates, 
        'time': time, 
    })
    return HttpResponse(template.render(context))
