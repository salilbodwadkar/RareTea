import numpy as np

# Define shift timings
shifts = ['Morning1', 'Morning2', 'Midday', 'Night1', 'Night2']
shift_start = [11.5, 11.5, 14, 17, 17]
shift_end = [17, 17, 19, 22, 22]

# Generate employee availability for the entire week
employee_availability = [np.random.randint(2, size=(10, len(shifts))) for _ in range(7)]

# Function to generate weekly schedules
def generate_weekly_schedules(employees, shifts, employee_availability):
    num_employees = len(employees)
    schedule = {employee: {shift: [] for shift in shifts} for employee in employees}

    for day_idx, day_availability in enumerate(employee_availability):
        assigned_shifts = {emp_idx: [] for emp_idx in range(num_employees)}

        for shift_idx, shift in enumerate(shifts):
            available_employees = [emp_idx for emp_idx in range(num_employees) if day_availability[emp_idx][shift_idx] == 1]
            np.random.shuffle(available_employees)

            for emp_idx in available_employees:
                if len(assigned_shifts[emp_idx]) >= 1:
                    continue  # Employee already has a shift for this day

                schedule[employees[emp_idx]][shift].append(f'Day {day_idx + 1}')
                assigned_shifts[emp_idx].append(shift_idx)
                break

    return schedule

# Test the scheduling function
employees = ['Employee1', 'Employee2', 'Employee3', 'Employee4', 'Employee5', 'Employee6', 'Employee7', 'Employee8', 'Employee9', 'Employee10']
weekly_schedules = generate_weekly_schedules(employees, shifts, employee_availability)

# Display generated schedules
for employee, shifts in weekly_schedules.items():
    print(f"{employee}:")
    for shift, days in shifts.items():
        print(f"{shift}: {', '.join(days)}")
    print()
    
