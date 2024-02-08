# Detailed syllabus breakdown for 45 lectures
# Allocating topics based on unit hours and total lectures

# Approximate topic distribution based on unit hours to total lectures
topics_per_unit = {
    "Unit 1": 8,  # 8 hours => Approx. 8 topics or 8 lectures
    "Unit 2": 11,  # 11 hours => Approx. 11 topics
    "Unit 3": 11,  # 11 hours => Approx. 11 topics
    "Unit 4": 8,  # 8 hours => Approx. 8 topics
    "Unit 5": 7,  # 7 hours => Approx. 7 topics
}

# Example topics for each unit, will adjust to ensure we have enough for a detailed plan
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

# Creating a detailed lecture plan
lecture_plan_detailed = []
lecture_no = 1

for unit, topics in unit_topics.items():
    for topic in topics:
        lecture_plan_detailed.append({
            "Lect. No.": lecture_no,
            "Chapter Name (Total Lectures)": unit,
            "Topic To be Uncovered / Details": topic
        })
        lecture_no += 1

# Convert to DataFrame for exporting to Excel
detailed_lecture_plan_df = pd.DataFrame(lecture_plan_detailed)

# Path to save the Excel file
detailed_excel_path = "/mnt/data/detailed_java_lecture_plan.xlsx"
detailed_lecture_plan_df.to_excel(detailed_excel_path, index=False)

detailed_excel_path
