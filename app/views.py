from django.shortcuts import render

# Create your views here.
def ifelif(request):
    d={'a':200,'b':300,'c':400}
    return render(request,'ifelif.html',d)
