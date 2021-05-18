from django.shortcuts import render
from .data import defCnt_list
# Create your views here.
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {'gubun_list': defCnt_list}
    return render(request, 'list.html', context)
