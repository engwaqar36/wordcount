from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'name':'This is waqar'})

def contact(request):
    return HttpResponse("<h1>Contact page</h1><br> This is our contact page")

def homepage1(request):
    return HttpResponse("<h1>This is homepage</h1>")

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_length= len(word_list)
    worddictionary ={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1
            
    worddictionary =sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':data, "words":list_length, "word_dic":worddictionary})