from django.urls import path

from . import views

app_name = 'leave'

urlpatterns = [
    path('', views.leave_request_list, name='leave_list'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('pending_leave_request/', views.pending_leave_requests, name='pending_leave_requests'),
    path('leave_request_approve/<int:id>/', views.leave_request_approve, name='leave_request_approve'),
    path('leave_request_reject/<int:id>/', views.leave_request_reject, name='leave_request_reject'),
]