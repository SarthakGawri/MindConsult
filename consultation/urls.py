from django.urls import path
from . import views

app_name = "consultation"

urlpatterns = [
    path('', views.index, name='index'),
    path('myconsultations', views.consultations, name='consultations'),
    path('new/<str:room_name>/', views.consultation, name='consultation')
]
