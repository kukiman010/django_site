from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
    #return HttpResponse("<h2>проверка</h2>")

def index(request):
    return render(request, 'mainApp/homePage.html')

