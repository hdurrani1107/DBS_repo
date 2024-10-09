import json
import pandas as pd
import random
import numpy as np
import re
import matplotlib.pyplot as plt

def distribution(gpa):
    
    if gpa >= 3.5:
        mean_grade = np.random.uniform(85, 100)
        variance = 5
    elif gpa >= 2.5:
        mean_grade = np.random.uniform(60, 90)
        variance = 10
    else:
        mean_grade = np.random.uniform(0, 80)
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
quizscore = pd.DataFrame()
for i in quizzes:
    quizframe['Quiz: ' + str(i+1)] = student_gpa.apply(distribution)
quizframe['Qz Score'] = quizframe.sum(axis=1)
quizframe['Max Score'] = 1000
quizscore['Quiz Score'] = quizframe['Qz Score'] / quizframe['Max Score']


#Homework Frame
homeworkDict = dict(dataDict['homework'])
homeworks = range(homeworkDict['count'])
homeworkframe = pd.DataFrame()
homeworkscore = pd.DataFrame()
for i in homeworks:
    homeworkframe['Homework: ' + str(i+1)] = student_gpa.apply(distribution)

homeworkframe['HW Score'] = homeworkframe.sum(axis=1)
homeworkframe['Max Score'] = 500
homeworkscore['Homework Score'] = homeworkframe['HW Score'] / homeworkframe['Max Score']

#Exam Frame
examDict = dict(dataDict['exam'])
exams = range(examDict['count'])
examframe = pd.DataFrame()
examscore = pd.DataFrame()
for i in exams:
    examframe['Exam: ' + str(i+1)] = student_gpa.apply(distribution)
    examscore[f"Exam: {i+1} Score"] = (
        examframe[f"Exam: {i+1}"] / 100
    )

quizweight = quizDict['total']
quizweight = quizweight/100
homeworkweight = homeworkDict['total']
homeworkweight = homeworkweight/100
examweight = examDict['total']

weights = pd.Series({"Exam 1 Score": 0.1, "Exam 2 Score": 0.2, 
                     "Exam 3 Score": 0.25,"Quiz Score": quizweight,
                     "Homework Score": homeworkweight,})
final_grade = pd.DataFrame(student_ids)
final_grade = pd.merge(final_grade, quizscore, left_index = True, right_index = True)
final_grade = pd.merge(final_grade, homeworkscore, left_index = True, right_index = True)
final_grade = pd.merge(final_grade, examscore, left_index = True, right_index = True)

final_grade['Course Grade'] = np.ceil((((weights['Quiz Score'] * final_grade['Quiz Score']) + (weights['Homework Score'] * final_grade['Homework Score']) + (weights['Exam 1 Score'] * final_grade['Exam: 1 Score']) + (weights['Exam 2 Score'] * final_grade['Exam: 2 Score']) + (weights['Exam 3 Score'] * final_grade['Exam: 3 Score'])) / 1)*100)
final_grade['Letter Grade'] = pd.cut(final_grade['Course Grade'],
                                     bins=[0,60,70,73,77,80,83,87,90,93,96,100],
                                     labels=['F','D','C-','C','C+','B-','B',
                                              'B+','A-','A','A+'])



grade_counts = final_grade["Letter Grade"].value_counts().sort_index()
plt.figure(0)
grade_counts.plot.bar()
final_gpa = pd.DataFrame()
final_gpa['GPA'] = pd.cut(final_grade['Course Grade'], bins=[0,60,70,73,77,80,83,87,90,93,96,100],
                                                      labels=[0,0.7,1.3,1.7,2.0, 
                                                              2.3,2.7,3.0,3.3,3.7,4.0])
plt.figure(1)
plt.scatter(final_gpa['GPA'], student_gpa)
plt.xlabel("Course GPA")
plt.ylabel("Incoming GPA")
plt.title("Scatter Plot")
final_grade.to_csv('student_grades.csv')

    


