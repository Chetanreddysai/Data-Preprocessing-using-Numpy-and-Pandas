import pandas as pd
import numpy as np

students = pd.read_csv("student_scores.csv")

math_marks = students["math_score"].to_numpy()

print("Mean :", np.mean(math_marks))
print("Median :", np.median(math_marks))
print("Maximum :", np.max(math_marks))
print("Minimum :", np.min(math_marks))

normalized = (
    (math_marks - math_marks.min())
    /
    (math_marks.max() - math_marks.min())
)

print(normalized)
