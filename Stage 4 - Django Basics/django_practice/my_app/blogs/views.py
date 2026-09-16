from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from django.conf import settings
import json
# Create your views here.

# # functional view 
def home(request):
    
    json_path = settings.STATICFILES_DIRS[0] / 'mock_data' / 'blogs_data.json'
    
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    # formatting date
    for blog in data:
        if blog['published_date']:
            blog['published_date'] = datetime.fromisoformat(blog['published_date'])

    return render(request, 'home.html' ,{'blogs': data})

def blogs_by_id(request,blog_id):
    return HttpResponse(f"Blog ID : {blog_id} Type: {type(blog_id).__name__}")

def blogs_by_slug(request,blog_slug):
    return HttpResponse(f"Blog slug : {blog_slug} Type: {type(blog_slug).__name__}")

def blogs_by_year(request,year):
    return HttpResponse(f"Year : {year}")


class UserView(View):
    def get(self,request):
        return HttpResponse("Hello User !!")
