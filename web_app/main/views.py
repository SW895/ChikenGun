from django.shortcuts import render
from .models import ArchiveVideo
from .forms import Video_created_date

# Create your views here.
def stream_view(request):
     return render(
        request,
        'stream_page.html',
    )

def main_view(request):
    return render(
        request,
        'main_page.html',
        context = {

        }
    )

def archive_view(request):
    if request.method == "POST":
        form = Video_created_date(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            videos = ArchiveVideo.objects.filter(date_created=date)
            #objects = form.cleaned_data['objects']
    else:       
        date = None
        #objects = None
        form = Video_created_date()
    return render(
        request,
        'archive_page.html',        
        context = {
           'form':form,
           'date':date,
           'videos':videos
           #'objects':objects,
        }
    )
