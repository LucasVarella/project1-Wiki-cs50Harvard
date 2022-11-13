from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import time
import random as rd
import markdown2 as mk
from . import util
from encyclopedia.newform import NewForm

data = ""
global_title = ""


def index(request):
    # Se for POST
    if request.method == "POST":
        data = request.POST['q']
        result =[]
        for entrie in util.list_entries():
            #Verifica se a pesquisa é igual á alguma página existente
            if str(data).upper() == entrie.upper():
                content = util.get_entry(data)
                content = mk.markdown(content)
                return render(request, "encyclopedia/greet.html", {
                    "title": data, "content": content

                })
            #Verifica se a pesquisa contem substrings presentes em títulos de páginas existentes
            elif (str(data).lower()) in entrie.lower():
                result.append(entrie)
        return render(request, "encyclopedia/search.html", {
            "result": result, "data": data
        })

    # se não for POST
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def greet(request, title):

    if request.method == "GET":
        content = util.get_entry(title)   
        content= mk.markdown(content)
        global global_title 
        global_title = title
        return render(request, "encyclopedia/greet.html", {
            "title": title, "content": content
        })
     

def edit(request):

    if request.method == "POST":
        form = NewForm()
        content = util.get_entry(global_title)


        return render(request, "encyclopedia/edit.html", {
            "title": global_title, "content": content, "form": form
        })
    
    else:

        form = NewForm()
        return render(request, "encyclopedia/edit.html", {"form": form})


def newPage(request):
    # Se for POST
    if request.method == "POST":
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
       
        if (title and content !="" ):
            if (not util.get_entry(title)):
                content = "# "+title+"\n" +content
                util.save_entry(title, content)
                msg = "Saved Successfully"
                return render(request, "encyclopedia/greet.html", {
            "content": mk.markdown(content)
        })
            else:
                msg = "This title already exists"
        else:
            msg = "Preencha"

        
        return render(request, "encyclopedia/newpage.html", {
            "msg": msg
        })


    return render(request, "encyclopedia/newpage.html")

def random(request):
    content_list = util.list_entries()
    random_title = rd.choice(content_list)
    random_content = util.get_entry(random_title)
    content = mk.markdown(random_content)
    
    return render(request, "encyclopedia/greet.html", {
        "title": random_title, "content": content
   })


