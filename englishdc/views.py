from django.shortcuts import render, redirect
from PyDictionary import PyDictionary 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    antonyms = dictionary.antonym(search)
    synonyms = dictionary.synonym(search)

    context = {

        'meaning': meaning['Noun'][0],
        'antonyms': antonyms,
        'synonyms': synonyms,
    }

    return render(request, 'word.html', context)