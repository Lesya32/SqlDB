from django.http import request
from django.shortcuts import render
from .models import Articles


def views(request):
    news = Articles.objects.all()
    print('views')
    return render(request, 'SQLDb/index.html', {'news': news})
