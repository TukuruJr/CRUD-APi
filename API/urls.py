from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Request, name="get"),
    path('<str:key>/', views.Detailed_Request, name="detailed"),
    path('create/', views.Create, name="post"),
    path('delete/<str:key>/', views.Delete, name="delete"),
]
