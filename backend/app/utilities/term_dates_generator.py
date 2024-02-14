from datetime import datetime, timedelta

def generate_class_dates(days_of_week, start_date, end_date, holidays):
    # Convert start and end dates to datetime objects
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    
    # Convert holiday strings to datetime objects
    holiday_dates = [datetime.strptime(date, "%d/%m/%Y") for date in holidays]
    
    # Weekdays in Python's datetime module are Monday=0, Sunday=6
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    
    # Convert days of the week to a list of weekday numbers
    weekday_numbers = [weekdays[day] for day in days_of_week]
    
    # Generate dates
    current_date = start
    class_dates = []
    
    while current_date <= end:
        if current_date.weekday() in weekday_numbers and current_date not in holiday_dates:
            class_dates.append(current_date.strftime("%d/%m/%Y"))
        current_date += timedelta(days=1)
    
    return class_dates

# Example usage
days_of_week = ["Monday"] # Days of the week for the class
term_start = "01/02/2024" # Term start date
term_end = "25/05/2024" # Term end date
holidays = ["26/01/2024", "08/03/2024", "25/03/2024", "29/03/2024", "10/04/2024", "11/04/2024", "17/04/2024", "10/05/2024"] # List of holidays

# Generate the list of class dates for all specified days of the week
class_dates = generate_class_dates(days_of_week, term_start, term_end, holidays)

# Print the list of class dates
print("Class dates:")
for date in class_dates:
    print(date)
