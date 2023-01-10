from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Views basado en funciones


def index(request):
    return HttpResponse('Hello World, from django')


def index_view(request):
    
    if request.method == "GET":
        print('GET')
    elif request.method == 'POST':
        print('POST')
    
    return HttpResponse('Index')



# Views basado en clases

class IndexView(View):

    def get(self, request):
        print('GET')
        return HttpResponse('Index Get')
    
    def post(self, request):
        print('POST')
        return HttpResponse('Index Post')
