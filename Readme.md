# Employee Roster App

This is a simple employee roster app built using Django. It helps to keep track of employees, their roles, shifts, leave requests, and holidays within an organization. The app includes several models to manage employee data, profiles, roles, shifts, leave requests, and holidays.

## Models

### 1. **User**
- **Description**: Keeps track of the employees in the organization.
- **Fields**:
  - `role`: The employee's role (e.g., Developer, QA, Manager).
  - `shift`: The shift assigned to the employee (e.g., Weekend, Regular, etc.).
  - `reports_to`: The reporting officer of the employee (ForeignKey to `User`).

### 2. **Employee Profile**
- **Description**: Stores miscellaneous information about the employee, which can be modified by the employee themselves.
- **Fields**:
  - `user`: ForeignKey reference to the `User` model.
  - `date_of_birth`: Employee's date of birth.
  - `phone_number`: Employee's contact number.
  - `address`: Employee's address.

### 3. **Role**
- **Description**: Stores the different roles within the organization.
- **Fields**:
  - `name`: The name of the role (e.g., Developer, Manager).
  - `access_level`: The access level associated with this role (e.g., Admin, User, Manager).

### 4. **Shift**
- **Description**: Stores the different shifts available for employees.
- **Fields**:
  - `name`: Name of the shift (e.g., Weekend, Regular).
  - `start_time`: The start time of the shift.
  - `end_time`: The end time of the shift.
  - `days_of_week`: Indexes of the days that are applicable for the shift (0 for Monday, 6 for Sunday).

### 5. **Holiday**
- **Description**: Stores the holidays in the organization.
- **Fields**:
  - `name`: Name of the holiday (e.g., Christmas, New Year's Day).
  - `date`: The date of the holiday.

### 6. **Leave Request**
- **Description**: Stores the list of leave requests made by employees.
- **Fields**:
  - `user`: ForeignKey reference to the `User` model (employee making the leave request).
  - `reason`: Reason for the leave request (e.g., personal, sick leave).
  - `date`: The date of the leave request.
  - `status`: The status of the leave request (e.g., Approved, Pending, Rejected).
  - `superior`: ForeignKey reference to the reporting officer (`User` model).


## Features:
- Upon log in the employee will be able to view the current month calendar holding info his shift days
- there is a button that takes the user to a page where they can modify their profile details
- there is a button in the home page that lets them view the list of all employees
- there is a button in the home page which takes them to the leave request page where they will be able to look at the history of their leave requests and status , from this page there is button to raise a new leave request and also if the logged employee has subordinates there is a button that shows the pending leave requests to approve/reject.
- New employees, shifts, holidays, roles are added from the admin page
