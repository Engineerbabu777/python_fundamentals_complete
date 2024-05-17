fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



for i in range(5):
    print(i)


student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for student, grade in student_grades.items():
    print(f"{student} got a grade of {grade}")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element)


colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index} is {color}")
