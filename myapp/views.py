from django.shortcuts import render


def index(request):
    return render(request, 'template.html')


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
