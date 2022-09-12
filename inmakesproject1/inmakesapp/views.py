from django.http import HttpResponse

from django.shortcuts import render

from . models import Place
from . models import Service
def demo(request):
    #fetching objects
    obj=Place.objects.all()
    ser=Service.objects.all()
    return render(request,"index.html",{'result':obj,'servic':ser})
# def demo(request):
#     name="india"
#      return render(request,"index1.html",{'obj':name})


# def addition(request):
#     x=int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     mod=x%y
#     return render(request,"result.html",{'result':res,'subtraction':sub,'multi':mul,'division':div,'modulus':mod})

