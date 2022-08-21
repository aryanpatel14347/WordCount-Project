from django.http import HttpResponse
from django.shortcuts import render
import operator
#from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'Home.html', {"title": "My first Website in Python"})

def count(request):
    fulltext = request.GET['myword']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1


    shortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{"title": "Count","fulltext": fulltext, "total_words": len(wordlist), 'worddictionary': worddictionary.items(), "shortedWords": shortedWords})
