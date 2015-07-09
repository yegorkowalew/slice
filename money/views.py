from django.http import HttpResponse
# from django.shortcuts import render
from django.template import RequestContext, loader

# def money(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

def money(request):
    money = 100
    template = loader.get_template('money.html')
    context = RequestContext(request, {
        'money': money,
    })
    return HttpResponse(template.render(context))
