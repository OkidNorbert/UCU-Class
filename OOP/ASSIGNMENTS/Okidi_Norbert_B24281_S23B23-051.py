#Okidi Norbert B24281 S23B23/051 BSCS
# Part (a)
def add_student(student_list, student_id, name, age, course):
    for student in student_list:
        if student['id'] == student_id:
            print("Error: Student ID already exists!")
            return
    student = {'id': student_id, 'name': name, 'age': age, 'course': course}
    student_list.append(student)

# Part (b)
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student
    print("Error: Student not found!")
    return None

def remove_student_by_id(student_list, student_id):
    for i, student in enumerate(student_list):
        if student['id'] == student_id:
            del student_list[i]
            return
    print("Error: Student not found!")

# Part (c)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# Demonstrating polymorphism
def demonstrate_polymorphism():
    student = Student("Okidi", 20, "Computer Science")
    instructor = Instructor("Norbert", 40, "Mathematics")

    student.study()
    instructor.teach()

# Part (d)
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

# Example Usage
students = [
    {'id': 1, 'name': "Okidi", 'age': 20, 'course': "Computer Science"},
    {'id': 2, 'name': "Norbert", 'age': 22, 'course': "Engineering"},
]

# Adding a new student
add_student(students, 3, "Aber", 21, "Mathematics")

# Finding a student by ID
print(find_student_by_id(students, 2))

# Removing a student by ID
remove_student_by_id(students, 1)

# Sorting students by age
sorted_by_age = sort_students(students, lambda x: x['age'])
print("Sorted by age:", sorted_by_age)

# Sorting students by name
sorted_by_name = sort_students(students, lambda x: x['name'])
print("Sorted by name:", sorted_by_name)

# Demonstrate polymorphism
demonstrate_polymorphism()
