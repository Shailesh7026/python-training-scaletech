from . import views
from django.urls import path,re_path

urlpatterns = [
    path('',views.home,name="home"),
    path('user/',views.UserView.as_view(),name="user"),
    
    # path prams
    path('<int:blog_id>/',views.blogs_by_id , name="blog_by_id"),
    path('slug/<str:blog_slug>/',views.blogs_by_slug, name="blog_by_slug"),
    
    # we can use re_path for regex based path validation
    re_path(r'^year/(?P<year>\d{4})/$', views.blogs_by_year, name="blogs_by_year")
]