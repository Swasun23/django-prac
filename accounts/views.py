from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from calendar import HTMLCalendar,monthrange
from datetime import datetime
from roster.models import Holiday
from .forms import ProfileEditForm
import re
from leave.models import LeaveRequest

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('accounts:home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('accounts:login')

@login_required
def profile(request):
    profile = request.user.profile  # Assuming a OneToOneField to the profile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def home_view(request):
    def generate_day_cell(day, style_attr, tooltip):
        # Create the base pattern to search for
        if day == 0:  # Handle empty cells
            original = '<td class="noday">&nbsp;</td>'
            return original
        
        # Create pattern that matches the existing td with the day number
        day_pattern = f'<td class="[^"]*">{day}</td>'
        
        # Create the replacement td with styles and tooltip
        replacement = f'<td class="[^"]*" style="{style_attr}">{day}{tooltip}</td>'
        
        return day_pattern, replacement

    # Get the current date
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    user = request.user

    # Get the current user's shift
    shift = request.user.shift

    # Get all holidays for the current month
    holidays_this_month = Holiday.objects.filter(date__month=current_month, date__year=current_year)

    #Get all approved leave requests for the current month
    leave_requests = LeaveRequest.objects.filter(user=user,date__month=current_month, date__year=current_year, status='approved')
    
    workdays = shift.days_of_week

    # Generate a calendar for the current month
    calendar = HTMLCalendar()
    calendar_html = calendar.formatmonth(current_year, current_month, withyear=True)

    # Get the number of days in the current month
    days_in_month = monthrange(current_year, current_month)[1]

    # Process each day of the month
    for day in range(1, days_in_month + 1):
        day_date = datetime(current_year, current_month, day)
        day_str = f">{day}<"
        styles = []  # Collect styles for this day
        tooltip_content = []  # Collect tooltip content for this day

        # Highlight weekends
        if day_date.weekday() not in workdays:  # Saturday or Sunday
            styles.append("background-color:lightgray")
            tooltip_content.append("Off day")
        else:
            # Highlight shift details on weekdays
            if shift:
                shift_info = f"{shift.start_time.strftime('%H:%M')} - {shift.end_time.strftime('%H:%M')}"
                tooltip_content.append(f"Shift: {shift_info}")
                styles.append("background-color:lightblue")

        # Highlight holidays
        for holiday in holidays_this_month:
            if holiday.date.day == day:
                tooltip_content.append(f"Holiday: {holiday.name}")
                styles.append("background-color:lightgreen")
        # Highlight leave requests
        for leave_request in leave_requests:
            if leave_request.date.day == day:
                tooltip_content.append(f"Leave: {leave_request.reason}")
                styles.append("background-color:yellow")

        # Combine styles and tooltip content
        style_attr = '; '.join(styles)
        tooltip = " ".join([f'<span class="tooltip">{item}</span>' for item in tooltip_content])

        # Replace the original day with styled and tooltip-enhanced HTML
        pattern, replacement = generate_day_cell(day, style_attr, tooltip)
        calendar_html = re.sub(pattern, replacement, calendar_html)

    # Render the calendar in the template
    return render(request, 'accounts/home.html', {
        'calendar': calendar_html,
    })
