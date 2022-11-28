from django.shortcuts import render
from webapp.models import Driver
# Create your views here.
def driverslist(request):
    items=Driver.objects.all()
    return render(request,'MyApp/Cardriverslist.html',{'items':items})
