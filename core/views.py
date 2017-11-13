from django.shortcuts import render
from django.http import HttpResponse


def index(requisicao):
    return render(requisicao,"index.html")

def lista_cursos(requisicao):
    return render(requisicao,"lista_cursos.html")

def noticias(requisicao):
    return render(requisicao,"noticias.html")

def contato(requisicao):
    return render(requisicao,"contato.html")

def cadastro(requisicao):
    return render(requisicao,"cadastro.html")

def novadisciplina(requisicao):
    return render(requisicao,"novadisciplina.html")

def login(requisicao):
    return render(requisicao,"login.html")

def detalhe_curso(requisicao):
    return render(requisicao,"detalhe_curso.html")

def disciplinas(requisicao):
    return render(requisicao,"disciplinas.html")

def esquecisenha(requisicao):
    return render(requisicao,"esquecisenha.html")