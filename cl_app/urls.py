from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.FormPage,name="temp"),
    path("regpage/",views.RegPage,name="regpage"),
    path("temp/",views.TempPage,name="temp"),

]