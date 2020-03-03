#-*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from todolist.models import Todo

def index(request):
    todos = Todo.objects.all()
    
    class Article:
        pass

    article = Article()
    article.author = 'MengChen Wang'
    article.title = 'MengChen write an aritle'
    article.source = 'https://www.baidu.com'
    article.description = 'xxxxxxxxx'

    articles = [article]

    article = Article()
    article.author = 'MengChen Wang'
    article.title = 'MengChen read an aritle'
    article.source = 'https://www.baidu.com'
    article.description = 'xxxxxxxxx'

    articles.append(article)

    count = 1
    for article in articles:
        article.odd = True if count % 2 == 1 else False
        count += 1

    return render(request, 'index.html', locals())
def complete(request, id):
    t=Todo.objects.get(id=id)
    t.completed=True
    t.save()
    return HttpResponseRedirect ('/')
def delete(request, id):
    t=Todo.objects.get(id=id)
    t.delete()
    return HttpResponseRedirect ('/')
def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Todo.objects.create(title=title, description=description)
    return HttpResponseRedirect ('/')
def edit(request, id):
    if request.method == "POST":
        t=Todo.objects.get(id=id)
        t.title = request.POST.get("title")
        t.description = request.POST.get("description")
        t.save
        return HttpResponseRedirect("/")