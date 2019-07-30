from django.urls import path

from .views import index



app_name = "hello"
urlpatterns = [path("", index, name="index"),
               ]
