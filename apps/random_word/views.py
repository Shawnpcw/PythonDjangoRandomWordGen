from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
  # the index function is called when root is visited
def index(request):
    context = {
        'random': get_random_string(length=14)
    }
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] +=1
    

    return render(request,'random_word/index.html', context)
def reset(request):
    del request.session['count']

    return redirect('/random_word')