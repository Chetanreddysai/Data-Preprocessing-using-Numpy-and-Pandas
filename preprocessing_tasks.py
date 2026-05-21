import pandas as pd

students = pd.read_csv("student_scores.csv")

students["math_score"].fillna(
    students["math_score"].mean(),
    inplace=True
)

students["science_score"].fillna(
    students["science_score"].mean(),
    inplace=True
)

students["exam_date"] = pd.to_datetime(
    students["exam_date"],
    errors="coerce"
)

students.drop_duplicates(inplace=True)

print(students)
