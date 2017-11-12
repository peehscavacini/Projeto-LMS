from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Faculdade Inovação Tecnologia'
    }
    return render(request, 'index.html', context)

