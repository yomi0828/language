from django.shortcuts import render
import datetime

# Create your views here.
def yomi(request):
    context = {'message':'yomi', 'time':datetime.datetime.now()}            
    return render(request, 'yomi/yomi.html', context)