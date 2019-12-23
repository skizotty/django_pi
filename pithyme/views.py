from django.http import HttpResponse
from django.shortcuts import render

context = {
    'one': '1234',
    'two': '12344'
}


def index(request):
    return render(request, 'template.html', context=context)
