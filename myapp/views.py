from django.shortcuts import render

from myapp.models import Board


def index(request):
    return render(request, 'template.html')


# Create your views here.

def homepage(request):
    count = Board.objects.all().count()
    count_img = Board.objects.filter(media_type='img').count()
    count_vid = Board.objects.filter(media_type='vid').count()
    context = {
        'total': count, 'total_img': count_img, 'total_vid': count_vid, 'page': 'Welcome to the board',}
    request.session['location']="unknown"
    if request.user.is_authenticated():
        request.session['location'] = "Earth"
    return render(request, 'base.html', context)
