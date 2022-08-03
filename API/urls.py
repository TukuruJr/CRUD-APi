from django.urls import path
from . import views

urlpatterns = [
    path('', views.Create, name="create"),
    path('get/', views.Get_Request, name="get"),
    path('<str:key>/', views.Detailed_Request, name="detailed"),
    path('update/<str:key>/', views.Update, name="update"),
    path('delete/<str:key>/', views.Delete, name="delete"),
]
