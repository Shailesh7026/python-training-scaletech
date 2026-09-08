from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

# functional view 
def home(request):
    return HttpResponse("Hello !!")

class UserView(View):
    def get(self,request):
        return HttpResponse("Hello User !!")
