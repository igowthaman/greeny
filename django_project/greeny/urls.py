from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Greeny"),
    path('home/', views.home, name="Greeny"),
    path('about/', views.about),
    path('terms-and-conditions/', views.terms),
    path('privacy-policy/', views.privacy),
    path('auth/', views.auth_func),
    path('auth-resp/', views.auth_resp),
]