from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('register', views.register, name='register'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('userlist', views.userlist, name='userlist'),
    path('patients', views.patientlist, name='patientlist'),
    path('search', views.patient_id, name='search'),
    path('delete', views.delete_patient, name='delete'),
    path('update', views.update, name='update'),
    path('update_patient', views.update_patient, name='update_patient'),
    path('create', views.add_patient, name='create'),
]