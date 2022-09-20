from app.views import home,HospitalDetailsView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',home, name='homepage'),
    path('hospital/<int:pk>', HospitalDetailsView.as_view(), name='hospital_detail'),

    
]
