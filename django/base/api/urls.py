from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.getUsers,name='api_users'),
    path('user/<str:pk>', views.getUser)
]