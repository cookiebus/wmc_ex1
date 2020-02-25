#-*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from todolist.models import Todo

def index(request):
    todos = Todo.objects.all()
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