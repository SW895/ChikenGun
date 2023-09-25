from django.shortcuts import render
from django.http import StreamingHttpResponse
from .utils import gen, VideoCamera

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
     return render(
        request,
        'archive_page.html',
        context = {
            
        }
    )