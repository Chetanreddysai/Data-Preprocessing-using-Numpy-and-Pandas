import pandas as pd

students = pd.read_csv("student_scores.csv")

students["average_score"] = (
    students["math_score"] +
    students["science_score"]
) / 2

top_students = students.sort_values(
    by="average_score",
    ascending=False
).head(5)

print(top_students)

correlation = students["attendance"].corr(
    students["average_score"]
)

print(correlation)

grouped = students.groupby("gender")[
    ["math_score", "science_score"]
].mean()

print(grouped)
