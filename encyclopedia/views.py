from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import markdown2
from django import forms
import os.path
import random
from django.urls import reverse
import string
import re

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,name):
    s = util.get_entry(name)
    if s==None:
        return HttpResponse("Entry Not Found!")
    else:
        html=markdown2.markdown(s)
        return render(request, "encyclopedia/entry.html", {
        "entry": html , "title":name
    })

def create(request):
    if request.method == "POST":
        title1=request.POST['title']
        text=request.POST['text']
        mj="Error: Please enter the Title."
        if title1=="":
            return render(request, "encyclopedia/create.html", {
        "error": mj ,  "title":title1 , "text":text
    })

        kj="Error: This Entry Already Exists" 
        for entry in util.list_entries():
            if title1 == entry:
                return render(request, "encyclopedia/create.html", {
        "error": kj ,  "title":title1 , "text":text
    })
        util.save_entry(title1,text)
        return title(request,title1)
    else:
        return render(request, "encyclopedia/create.html")

def randomx(request):
    entries = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse('title',args=[f'{entries}']))

def search(request):
    value=request.GET['q']
    s = util.get_entry(value)
    if s==None:
        ulo=[]
        entries=util.list_entries()
        for entry in entries:
            for sk in range(len(entry)):
                if sk+1>len(entry):
                    break
                if value.lower()==entry[0:sk+2].lower():
                    ulo.append(entry)

        return render(request, "encyclopedia/search.html", {
        "entries": ulo
    })
                    


    else:
        return HttpResponseRedirect(reverse('title',args=[f'{value}']))

def edit(request):
    if request.method == "POST":
        title1=request.POST['title']
        text=request.POST['text']
        util.save_entry(title1,text)
        return title(request,title1)
    else:
        en=util.get_entry(request.GET['title'])
        return render(request, "encyclopedia/edit.html", {
            "title":request.GET['title']  , "entry":en
        })
        
    
        

