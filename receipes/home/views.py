from django.shortcuts import render
from .models import *


# Create your views here.

def receipe(request):
    if request.method=="POST":
        data=request.POST
        receipe_img=request.FILES.get('receipe_img')
        receipe_name=data.get('receipe_name')
        receipe_desc=data.get('receipe_desc')
        Receipe.objects.create(
            receipe_img=receipe_img,
            receipe_name=receipe_name,
            receipe_desc=receipe_desc,
        )

       
        print(receipe_name)
        print(receipe_desc)
        print(receipe_img)

    return render(request,'index.html')

