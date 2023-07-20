from django.urls import path
from .views import BlogListView

app_name="blog"

urlpatterns = [
    
    path('hi/', BlogListView.as_view(), name="homeview")
    
]
