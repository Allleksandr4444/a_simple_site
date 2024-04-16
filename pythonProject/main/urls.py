from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.text),
   path('sheettwo/', views.text2)
]