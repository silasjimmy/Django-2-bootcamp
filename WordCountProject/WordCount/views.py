from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
    return render(request, "index.html")

def count(request):
    fullText = request.GET['fulltext']

    wordlist = fullText.split()

    wordDict = {}

    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fullText': fullText, 'count': len(wordlist), 'sortedWords': sortedWords})

def about(request):
    return render(request, "about.html")
