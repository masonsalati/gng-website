from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('review/', views.review, name='review'),
]

