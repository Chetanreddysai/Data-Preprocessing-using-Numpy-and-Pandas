import pandas as pd

students = pd.read_csv("student_scores.csv")

print(students.head())

print(students.dtypes)

print(students.isnull().sum())

attendance_data = students[
    students["attendance"] < 70
]

print(attendance_data)
