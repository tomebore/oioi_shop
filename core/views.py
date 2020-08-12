from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("homepage.html")

def test(request):
    return HttpResponse("test.html")