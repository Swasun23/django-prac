from django.urls import path
from . import views

app_name = 'roster'

urlpatterns = [
    path('all_employees/', views.view_roster, name='view_roster'),
]