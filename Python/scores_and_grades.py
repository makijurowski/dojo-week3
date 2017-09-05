'''This is a Coding Dojo homework assignment.'''

import random


def scores_and_grades(students):
    '''This function generates test scores for a number of students,
    and then prints a grade report for each student.'''

    # Declare variables including dictionary object with grading scale.
    scoreList = []
    gradeDict = {'A': '90,100', 'B': '80,89', 'C': '70,79', 'D': '60,69'}

    # Generate random grades between 60-100 for each student.
    for i in range(0, (students - 1)):
        scoreList.append(random.randint(60, 100))
    print scoreList

    # Print out score report including letter grade for each student
    for score in scoreList:
        for grade, scale in gradeDict.iteritems():
            low, high = scale.split(',', 1)
            if int(low) <= score <= int(high):
                print 'Score: ' + str(score) + '; Your grade is: ' + grade

    return 'All finished!'

print(scores_and_grades(10))
