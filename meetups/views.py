from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(req):
    return render(req, 'meetups/index.html')
    # settings.py templates=[dir] has some importance which is discussed in main course