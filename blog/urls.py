from django.urls import path
from .views import BlogListView, BlogCreateView

app_name="blog"

urlpatterns = [
    
    path('list/', BlogListView.as_view(), name="homeview"),
    path("create/", BlogCreateView.as_view(), name="create")
]
