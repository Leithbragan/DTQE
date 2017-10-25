from django.shortcuts import render
from dictionary.models import *


# Create your views here.


def big_dictionary(request):
    args = {}
    if request.method == 'GET':
        translations = Translation.objects.order_by("word_value__first_letter")
        args['words'] = translations
    return render(request, "dictionary/big_dictionary.html", args)


def page_letter(request, first_letter):
    words = Word.objects.filter(first_letter=first_letter)
    # translations = Translation.objects.filter(word_value=[elem for elem in words])
    return render(request, "dictionary/page_letter.html", {'words': words})
