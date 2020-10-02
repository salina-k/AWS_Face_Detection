from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def ImageUploadView (request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageUploadForm()
    return render (request, 'forms.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


# view for displaying images

def display_upload_images(request):
    if request.method == 'GET':
        images = ImageUpload.objects.all()
        return render((request, 'display_upload_images.html', {'employee_images': images}))

