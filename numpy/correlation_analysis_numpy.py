
import numpy as np

# Student study hours and exam marks
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exam_marks = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Calculate correlation
correlation = np.corrcoef(study_hours, exam_marks)[0, 1]

# Calculate basic statistics
average_hours = np.mean(study_hours)
average_marks = np.mean(exam_marks)

print("STUDENT PERFORMANCE ANALYSIS")
print("-" * 35)

print("Study Hours:", study_hours)
print("Exam Marks:", exam_marks)

print("\nAverage Study Hours:", average_hours)
print("Average Exam Marks:", average_marks)

print("\nCorrelation Coefficient:", round(correlation, 2))

if correlation > 0:
    print("Result: Positive correlation")
elif correlation < 0:
    print("Result: Negative correlation")
else:
    print("Result: No linear correlation")

print("\nConclusion:")
if correlation > 0.7:
    print("More study hours are strongly associated with higher marks.")
elif correlation < -0.7:
    print("More study hours are strongly associated with lower marks.")
else:
    print("The relationship between study hours and marks is weak.")
