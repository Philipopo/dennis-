from django.urls import path
from . import views                                                                                 


urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('products/', views.products),
    path('customers/', views.customers),

]