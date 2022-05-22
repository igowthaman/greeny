from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Greeny"),
    path('home/', views.home, name="Greeny"),
    path('about/', views.about),
    path('terms/', views.terms),
    path('privacy/', views.privacy),
    path('auth/', views.auth_func),
    path('auth-resp/', views.auth_resp),
]