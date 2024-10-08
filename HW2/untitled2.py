import json
import pandas as pd
import random
import numpy as np
import re

def distribution(gpa):
    
    if gpa >= 3.5:
        mean_grade = np.random.uniform(85, 100)
        variance = 5
    elif gpa >= 2.5:
        mean_grade = np.random.uniform(60, 100)
        variance = 10
    else:
        mean_grade = np.random.uniform(0, 100)
        variance = 20
    
    grades = np.random.normal(mean_grade, variance, 1)
    # Clip grades between 0 and 100
    grades = np.clip(grades, 0, 100)
    return grades

    


dataframe = pd.DataFrame
student_info = pd.read_csv('student_information.csv')
student_info = pd.DataFrame(student_info)
student_ids = student_info['student_id']
student_gpa = student_info['GPA']

with open("student_assessment.json", 'r') as file:
    dataDict = json.load(file)

#Quiz Frame
quizDict = dict(dataDict['quiz'])
quizzes = range(quizDict['count'])
quizframe = pd.DataFrame()
for i in quizzes:
    quizframe['Quiz: ' + str(i+1)] = student_gpa.apply(distribution)

print(quizframe)

#Homework Frame
homeworkDict = dict(dataDict['homework'])
homeworks = range(homeworkDict['count'])
homeworkframe = pd.DataFrame()
for i in homeworks:
    homeworkframe['Homework: ' + str(i+1)] = student_gpa.apply(distribution)
print(homeworkframe)

#Exam Frame
examDict = dict(dataDict['exam'])
exams = range(examDict['count'])
examframe = pd.DataFrame()
for i in exams:
    examframe['Exam: ' + str(i+1)] = student_gpa.apply(distribution)
print(examframe)    
    

    


