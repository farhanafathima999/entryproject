from django.shortcuts import redirect, render
from django.http import HttpResponse
from imageapp.forms import UserImageForm
from .models import UploadImage


def home(request):
    form = UserImageForm()
    return render(request, 'index.html',{'form':form})


def image_save(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserImageForm()
    return render(request, 'index.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def image_show(request)  :
        if request.method == 'GET':
            img_object = UploadImage.objects.all()
            return render(request, 'index.html', {'img_obj': img_object})

