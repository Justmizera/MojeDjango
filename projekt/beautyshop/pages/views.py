from django.shortcuts import render


# Create your views here.

## tu są widoku moich podstron

def home_view(request):



    return render(request,'index.html')

