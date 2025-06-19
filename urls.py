from django.urls import path
from polls import views

urlpatterns= [
    path('', views.index, name='index'),
    path('address/', views.address_view, name='address'),
    path('phone/', views.phone_view, name='phone')
]