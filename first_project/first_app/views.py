from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello Class')
    my_data = {'insert_here':"I am coming from view"}
    return render(request, 'first_app/index.html', context=my_data)
