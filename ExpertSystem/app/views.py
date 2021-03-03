from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from .models import fact,solution
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)

def index(request):
    return HttpResponse("Hello, Django!")

# Create your views here.

def index(request):
    return render(request,'app/index.html')


def problem(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    fact_list = fact.objects.all()
   
    return render(
        request,
        'app/problem.html',
        {
            'title':'problems',
            'fact_list': fact_list,
        }
        
    )

      


