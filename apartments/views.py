from django.http import HttpResponse
from django.shortcuts import render
from .models import Rental
from django.template import loader

# Create your views here.
def index(request):
    rentals = Rental.objects.all()
    template = loader.get_template('index.html')
    print(rentals)
    context = {
        'rentals': rentals
    }
    # template.render(context, request)
    return HttpResponse(template.render())
    # return HttpResponse("Hello world")
