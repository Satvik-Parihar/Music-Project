from django.shortcuts import render
from .models import Music
# Create your views here.
def home(request):
    search=request.GET.get('song')
    songs=None
    search_performed=False
    if search:
        songs=Music.objects.filter(song__icontains=search)
        search_performed=True
    all_songs=Music.objects.all()
    context={
        'songs':songs,
        'all_songs':all_songs,
        'search_performed':search_performed,
        'search':search
    }
    return render(request,'home.html',context)