# roster/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from roster.models import Role, Shift, Holiday
from accounts.models import Employee_profile
from datetime import date, time

User = get_user_model()

class Command(BaseCommand):
    help = 'Loads initial data required for the roster application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading initial data...')

        # Create roles
        roles_data = [
            {'name': 'HR', 'access_level': 1},
            {'name': 'Employee', 'access_level': 0},
            {'name': 'Manager', 'access_level': 2},
            {'name': 'Team Lead', 'access_level': 1},
        ]

        for role_info in roles_data:
            Role.objects.get_or_create(
                name=role_info['name'],
                defaults={'access_level': role_info['access_level']}
            )
        self.stdout.write('Roles created successfully')

        # Create basic shifts
        shifts_data = [
            {
                'name': 'Morning Shift',
                'start_time': time(6, 0),  # 06:00
                'end_time': time(14, 0),   # 14:00
                'date': date.today()
            },
            {
                'name': 'Afternoon Shift',
                'start_time': time(14, 0),  # 14:00
                'end_time': time(22, 0),    # 22:00
                'date': date.today()
            },
            {
                'name': 'Night Shift',
                'start_time': time(22, 0),  # 22:00
                'end_time': time(6, 0),     # 06:00
                'date': date.today()
            },
            {
                'name': 'Regular Day Shift',
                'start_time': time(9, 0),   # 09:00
                'end_time': time(17, 0),    # 17:00
                'date': date.today()
            }
        ]

        for shift_info in shifts_data:
            Shift.objects.get_or_create(
                name=shift_info['name'],
                defaults={
                    'start_time': shift_info['start_time'],
                    'end_time': shift_info['end_time'],
                    'date': shift_info['date']
                }
            )
        self.stdout.write('Shifts created successfully')

        # Create holidays (example for US holidays)
        holidays_data = [
            {
                'name': "New Year's Day",
                'date': date(date.today().year, 1, 1),
                'description': "New Year's Day Holiday"
            },
            {
                'name': 'Labor Day',
                'date': date(date.today().year, 9, 1),  # Approximate
                'description': 'Labor Day Holiday'
            },
            {
                'name': 'Christmas',
                'date': date(date.today().year, 12, 25),
                'description': 'Christmas Day'
            }
        ]

        for holiday_info in holidays_data:
            Holiday.objects.get_or_create(
                name=holiday_info['name'],
                date=holiday_info['date'],
                defaults={'description': holiday_info['description']}
            )
        self.stdout.write('Holidays created successfully')

        self.stdout.write(self.style.SUCCESS('Successfully loaded all initial data'))