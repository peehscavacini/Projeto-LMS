from django.shortcuts import render

from core.models import Curso, Aluno
from core.forms import ContatoForm, CursoForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def contato(request):
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()

    contexto = {
        "form":form
    }
    return render(request,"contato.html",contexto)


def curso(request):
    contexto= {
        "form":form
    }
    return render(request,"curso.html", contexto)


def lista_cursos(request):
    return render(request,"lista_cursos.html")

def noticias(request):
    return render(request,"noticias.html")

def cadastro(request):
    return render(request,"cadastro.html")

def novadisciplina(request):
    return render(request,"novadisciplina.html")

def login(request):
    return render(request,"login.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def interface(request):
    contexto = {
        "usuario":Aluno.objects.all(),
        "ra":Aluno.objects.all(),
        "perfil":"aluno",
        "cursos": Curso.objects.all(),
    }
    return render(request,"interface.html", contexto)

def disciplinasnovo(request):
    return render(request,"disciplinasnovo.html")

def PaginaAluno(request):
    return render(request,"PaginaAluno.html")

def smartclass(request):
    return render(request,"smartclass.html")

def TabelaNotasFaltas(request):
    return render(request,"TabelaNotasFaltas.html")