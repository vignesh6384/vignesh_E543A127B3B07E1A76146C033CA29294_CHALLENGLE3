class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    # Create a list of Student objects
    students = [
        Student("Alice", "A001", 3.7),
        Student("Bob", "B002", 3.9),
        Student("Charlie", "C003", 3.5),
        Student("David", "D004", 4.0),
        Student("Eve", "E005", 3.8)
    ]

    # Sort the students based on CGPA
    sorted_students = sort_students(students)

    # Display the sorted list of students
    print("Sorted Students (Descending Order of CGPA):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

