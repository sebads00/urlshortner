from django.shortcuts import render, redirect
from .models import Url
import uuid
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

    
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)