from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='resume_home'),
    path('about/', views.about, name='resume_about'),
]
