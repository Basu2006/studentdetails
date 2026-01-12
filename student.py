# student.py

def calculate_grade(marks):
    if marks >= 90:
        return "S"
    elif marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Optional: test data for running manually
if __name__ == "__main__":
    # Sample data
    students = [
        {"name": "Basu", "marks": 95},
        {"name": "Basu", "marks": 85},
        {"name": "Basu", "marks": 70},
        
    ]

    for student in students:
        grade = calculate_grade(student["marks"])
        print(f"Student: {student['name']}, Marks: {student['marks']}, Grade: {grade}")
