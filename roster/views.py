from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import login_required

@login_required
def view_roster(request):
    employees = User.objects.all()
    return render(request, 'roster/employee_roster.html', {'employees': employees})

# # roster/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from datetime import datetime, timedelta
# from calendar import monthcalendar
# from .models import Schedule, Holiday, Shift
# from accounts.models import Employee_profile

# @login_required
# def calendar_view(request):
#     today = timezone.now()
#     current_month = today.month
#     current_year = today.year
    
#     # Get employee's schedule for the current month
#     employee_schedule = Schedule.objects.filter(
#         employee=request.user.profile,
#         shift__date__year=current_year,
#         shift__date__month=current_month
#     ).select_related('shift')
    
#     # Get holidays for the current month
#     holidays = Holiday.objects.filter(
#         date__year=current_year,
#         date__month=current_month
#     )
    
#     # Create calendar data
#     calendar_data = []
#     for week in monthcalendar(current_year, current_month):
#         week_data = []
#         for day in week:
#             if day == 0:
#                 week_data.append(None)
#             else:
#                 date = datetime(current_year, current_month, day).date()
#                 shifts = employee_schedule.filter(shift__date=date)
#                 holiday = holidays.filter(date=date).first()
#                 week_data.append({
#                     'day': day,
#                     'shifts': shifts,
#                     'holiday': holiday,
#                 })
#         calendar_data.append(week_data)
    
#     context = {
#         'calendar_data': calendar_data,
#         'month': today.strftime('%B %Y'),
#     }
#     return render(request, 'roster/calendar.html', context)

# @login_required
# def employee_list_view(request):
#     employees = Employee_profile.objects.select_related('user', 'shift').all()
#     return render(request, 'roster/employee_list.html', {'employees': employees})
