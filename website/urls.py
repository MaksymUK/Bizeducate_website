from django.urls import path
from website.views import Index


urlpatterns = [
    path("",index, name="index")
]