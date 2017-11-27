"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin



from core.views import index, contato, lista_cursos, noticias, cadastro, novadisciplina, login, detalhe_curso, interface, disciplinasnovo, PaginaAluno, smartclass, TabelaNotasFaltas, curso




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index ),
    url(r'^contato/', contato ),
    url(r'^lista_cursos/', lista_cursos ),
    url(r'^noticias/', noticias ),
    url(r'^cadastro/', cadastro ),
    url(r'^novadisciplina/', novadisciplina ),
    url(r'^login/', login ),
     url(r'^detalhe_curso/', detalhe_curso ),
     url(r'^interface/', interface),
     url(r'^disciplinasnovo/', disciplinasnovo),
    url(r'^PaginaAluno/', PaginaAluno),
    url(r'^smartclass/', smartclass),
    url(r'^TabelaNotasFaltas/', TabelaNotasFaltas),
    url(r'^curso/', curso),




]


