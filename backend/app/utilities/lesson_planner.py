import pandas as pd
from datetime import datetime, timedelta

# Convert string dates to datetime objects
def str_to_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y")

# Define holidays
holidays = ["26/01/2024", "08/03/2024", "25/03/2024", "29/03/2024", "10/04/2024", "11/04/2024", "17/04/2024", "10/05/2024"]
holidays = [str_to_date(date) for date in holidays]

# Define the topics for each unit
unit_topics = {
    "Unit 1": [
        "Introduction to Java and its history",
        "Features of Java",
        "JVM, JRE, and JDK",
        "Setting up Java environment",
        "Basic syntax of Java",
        "Data types and variables",
        "Operators in Java",
        "Control flow statements"
    ],
    "Unit 2": [
        "Introduction to OOPs concepts",
        "Classes and Objects",
        "Constructors and Destructors",
        "Inheritance in detail",
        "Polymorphism",
        "Abstraction",
        "Encapsulation",
        "Interfaces",
        "Packages",
        "Static and Final",
        "Access Modifiers"
    ],
    "Unit 3": [
        "Inheritance types and usage",
        "Using packages for modular code",
        "Interfaces and their importance",
        "Abstract classes vs Interfaces",
        "Nested and Inner classes",
        "Overriding and Overloading",
        "Object class methods",
        "Generics",
        "Enumerations",
        "Annotations",
        "Reflection"
    ],
    "Unit 4": [
        "Introduction to exceptions",
        "Exception handling mechanism",
        "Try-catch-finally blocks",
        "Creating custom exceptions",
        "Introduction to multithreading",
        "Creating threads using Thread class and Runnable interface",
        "Thread synchronization",
        "Inter-thread communication"
    ],
    "Unit 5": [
        "File handling in Java",
        "Input and Output streams",
        "Reading from and writing to files",
        "Introduction to Collections framework",
        "List, Set, Map interfaces",
        "Commonly used Collections classes",
        "Iterators and Comparators"
    ],
}

# Generate lecture dates considering holidays and weekdays
def generate_lecture_dates(start_date, end_date, holidays, weekdays):
    current_date = start_date
    lecture_dates = []

    while current_date <= end_date:
        if current_date.weekday() in weekdays and current_date not in holidays:
            lecture_dates.append(current_date)
        current_date += timedelta(days=1)
    
    return lecture_dates

# Flatten topics for planning
topics = []
for unit, topics_list in unit_topics.items():
    for topic in topics_list:
        topics.append({"unit": unit, "topic": topic})

# Plan lessons based on topics and available lecture dates
def plan_lessons(topics, start_date, end_date, holidays, weekdays):
    # Adjusted to include CO values directly in the topics list
    lecture_dates = generate_lecture_dates(start_date, end_date, holidays, weekdays)
    lectures = []
    
    co_mapping = {"Unit 1": "CO1", "Unit 2": "CO2", "Unit 3": "CO3", "Unit 4": "CO4", "Unit 5": "CO5"}
    
    for i, topic in enumerate(topics, start=1):
        if i <= len(lecture_dates):
            lecture_date = lecture_dates[i-1].strftime('%Y-%m-%d')
            lectures.append({
                "Lect. No.": i,
                "Chapter Name (Total Lectures)": topic["unit"],
                "Topic To be Uncovered / Details": topic["topic"],
                "CO": co_mapping.get(topic["unit"], ""),  # Assign CO based on unit
                "Planned Date": lecture_date,
                "Perform Date": "",
                "Remark": "",
            })
    
    return lectures

# Define term dates and weekdays (Monday=0, Tuesday=1, ..., Sunday=6)
start_date = datetime(2024, 2, 1)
end_date = datetime(2024, 5, 25)
weekdays = [0, 1, 2]  # Monday, Tuesday, Wednesday

# Generate the lesson plan
lesson_plan = plan_lessons(topics, start_date, end_date, holidays, weekdays)

# Create DataFrame and save to Excel
lesson_plan_df = pd.DataFrame(lesson_plan)
lesson_plan_df.to_excel("complete_lesson_plan.xlsx", index=False)

print("Lesson plan generated successfully.")
