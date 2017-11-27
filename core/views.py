from django.shortcuts import render


# Create your views here.

def index(request):
    contexto = {
        "usuario":None,
        "perfil":"aluno",
        "cursos":[
            {"nome":"Desenvolvimento de Sistemas", "tipo":"Graduação"},
            {"nome":"Banco de Dados", "tipo":"Graduação"},
            {"nome":"Sistemas de Informação", "tipo":"Graduação"},
            {"nome":"Internet das Coisas", "tipo":"Pós Graduação"}
        ]
    }
    
    return render(request,"index.html", contexto)

def contato(request):
    return render(request,"contato.html")

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
        "usuario":None,
        "perfil":"aluno",
        "cursos":[
            {"nome":"Desenvolvimento de Sistemas", "tipo":"Graduação"},
            {"nome":"Banco de Dados", "tipo":"Graduação"},
            {"nome":"Sistemas de Informação", "tipo":"Graduação"},
            {"nome":"Internet das Coisas", "tipo":"Pós Graduação"}
        ]
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