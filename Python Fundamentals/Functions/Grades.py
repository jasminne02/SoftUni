grade = 0
while grade > 6 or grade < 2:
    grade = float(input())


def grader(grade_check):
    if 2 <= grade_check <= 2.99:
        return 'Fail'
    elif 3 <= grade_check <= 3.49:
        return 'Poor'
    elif 3.50 <= grade_check <= 4.49:
        return 'Good'
    elif 4.50 <= grade_check <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_check <= 6:
        return 'Excellent'


print(grader(grade))
