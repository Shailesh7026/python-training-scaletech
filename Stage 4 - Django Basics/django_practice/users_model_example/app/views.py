from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.

def add_user(request):
    if request.method != "POST":
        return render(request, 'user_form.html' , {"form":UserForm()})
    
    form = UserForm(request.POST)
    
    if form.is_valid():
        user = form.save()
        return HttpResponse(f"User created as {user.name}-{user.email}")
    
    return render(request, "user_form.html", {"form": form})

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method != "POST":
        form = UserForm(instance=user)
        return render(request, 'user_form.html', {"form": form})
    
    form = UserForm(request.POST,instance=user)
        
    if form.is_valid():
        user = form.save()
        return HttpResponse(f"User updated as {user.name}-{user.email}-{user.age}")
        
    return render(request, "user_form.html", {"form": form})
    
    
def list_user(request):  
        users = User.objects.all()
        return render(request, 'list_users.html',{'users':users})