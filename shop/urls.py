from django.urls import path
from . import views 

urlpatterns = [
    path('', views.shop_all, name='shop') #name is what you reference in the html file
]