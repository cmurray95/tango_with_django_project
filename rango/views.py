from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    # Retrieve top 5 categories from DB
    category_list = Category.objects.order_by('-likes')[:5]
    # Template vars
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context=context_dict)