from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
   # return HttpResponse('<b>hello')
   return render(request, 'home.html')

def eggs(request):
    
    return HttpResponse("Eggs")

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordDictionary = {}
    
    for word in wordlist:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            # add
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
   

    return render(request, 'count.html', {'fulltext': fulltext, 'length': len(wordlist), 'sortedWords':sortedWords})