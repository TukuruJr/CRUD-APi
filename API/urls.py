from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Request, name="get"),

]
