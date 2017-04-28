import random

from hello.models import Condition
from django.shortcuts import render
from django.http import HttpResponse
from itertools import permutations
from .models import Greeting

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    lista = Condition.objects.filter(number=2)
    condi = random.choice(lista)
    return render(request, 'index.html', {'condition': condi})

def colocar_no_banco_de_dados(request):
    Condition.objects.all().delete()
    for number in range(1,3):
        a = permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:number], number)
        for it in a:
            shuffled = "".join(it)
            Condition.objects.create(number=number, shuffled=shuffled)
    return HttpResponse('Done!')



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
