from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LeaveRequestForm
from .models import LeaveRequest
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
@login_required
def leave_request(request):
    user = request.user
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = user

            print(f"User {user.username} reports to {user.reports_to}")
            # Ensure the user has a supervisor
            if user.reports_to:
                leave_request.superior = user.reports_to
            else:
                # Handle the case where the user doesn't have a supervisor
                return render(request, 'leave/leave_request.html', {'form': form, 'error': "You do not have a supervisor assigned."})
            
            leave_request.save()

            # Use Django messages framework to show success
            messages.success(request, "Leave request submitted successfully")

            return redirect('leave:leave_list')  # Redirect to the leave list page
    else:
        form = LeaveRequestForm()

    return render(request, 'leave/leave_request.html', {'form': form})

@login_required
def leave_request_list(request):
    user = request.user
    leave_requests = user.leave_requests.all
    has_subordinates = user.subordinates.exists()

    return render(request, 'leave/leave_request_list.html', {'leave_requests': leave_requests, 'has_subordinates': has_subordinates})

#incase of superior we need a view viewing pending leave requests
@login_required
def pending_leave_requests(request):
    user = request.user
    #leave_requests = user.leave_requests_to_approve.filter(status='pending')
    leave_requests = LeaveRequest.objects.filter(superior=user, status='pending')
    return render(request, 'leave/leave_request_list_superior.html', {'leave_requests': leave_requests})

@login_required
def leave_request_approve(request, id):
    try:
        leave_request = LeaveRequest.objects.get(id=id)
        leave_request.status = 'approved'
        leave_request.save()
    except LeaveRequest.DoesNotExist:
        # Handle the case where the leave request doesn't exist
        return redirect('leave:pending_leave_requests')
    
    return redirect('leave:pending_leave_requests')

@login_required
def leave_request_reject(request, id):
    try:
        leave_request = LeaveRequest.objects.get(id=id)
        leave_request.status = 'rejected'
        leave_request.save()
    except LeaveRequest.DoesNotExist:
        # Handle the case where the leave request doesn't exist
        return redirect('leave:pending_leave_requests')
    
    return redirect('leave:pending_leave_requests')
