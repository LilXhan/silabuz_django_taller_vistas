from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime

# Tarea

class View1(View):

    name = 'Flavio'
    born_date = datetime.datetime(2002, 5, 4)
    actual_date = datetime.datetime.now()
    age = actual_date - born_date
    age = age.days
    age = int(age / 365)

    def get(self, request):
        
        context = {
            'name': self.name,
            'age': self.age 
        }

        return render(request, 'vista1.html', context )


class View2(View):

    name = 'Flavio'
    numbers = [i for i in range(1, 5)]

    def get(self, request):    

        context = {
            'name': self.name,
            'numbers': self.numbers
        }

        return render(request, 'vista2.html', context)


# Views basado en funciones


def index(request):
    
    return render(request, 'index.html', {})

    # return HttpResponse('Hello World, from django')


def index_view(request):
    
    if request.method == "GET":
        print('GET')
        
    elif request.method == 'POST':
        print('POST')
        return HttpResponse('POST')
    
    context = {
        'name': 'Flavio'
    }

    # return HttpResponse('Index')
    return render(request, 'index.html', context)



# Views basado en clases

class IndexView(View):

    template = 'index.html'
    context = {
        'name': 'Flavio'
    }

    def get(self, request):
        print('GET')
        return render(request, self.template, self.context)
        # return HttpResponse('Index Get')
    
    def post(self, request):
        print('POST')
        return HttpResponse('Index Post')
