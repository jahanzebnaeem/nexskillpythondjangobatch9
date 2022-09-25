from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # return HttpResponse('Hello Class')
    # my_data = {'insert_here':"I am coming from view"}
    # return render(request, 'first_app/index.html', context=my_data)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
