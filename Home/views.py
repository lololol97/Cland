from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def initial(request):
    return HttpResponse("<h1> Hi Rishit, \n if you are seeing this then I decided we need to make a fresh new website because i have imporved my django skills and JavaScript skills  </h1>")