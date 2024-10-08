import json
import pandas as pd
import random
import numpy as np
import re

dataframe = pd.DataFrame
student_info = pd.read_csv('student_information.csv')
student_info = pd.DataFrame(student_info)
student_info = student_info.sort_values(by='GPA', ascending=False)
student_ids = student_info['student_id']
student_status = student_info['status']
student_gpa = student_info['GPA']

student_info.reset_index(drop=True,inplace=True)
print(student_info)

try:
    with open("student_assessment.json", 'r') as file:
        dataDict = json.load(file)
except:
    with open("assessment_information.json", 'r') as file:
        dataDict = json.load(file)
        
quizDict = dict(dataDict['quiz'])
quizCompletes = list(quizDict['completes'])
quizDistList = list(quizDict['grades'][0])

homeworkDict = dict(dataDict['homework'])
homeworkCompletes = list(homeworkDict['completes'])
homeworkDistList1 = list(homeworkDict['grades'][0])
homeworkDistList2 = list(homeworkDict['grades'][1]) 

examDict = dict(dataDict['exam'])
examCompletes = list(examDict['completes'])
examDistList1 = list(examDict['grades'][0])
examDistList2 = list(examDict['grades'][1])
examDistList3 = list(examDict['grades'][2])


# def distribution(gpa):
    
#     if gpa >= 3.5:
#         mean_grade = np.random.uniform(85, 100)
#         variance = 5
#     elif gpa >= 2.5:
#         mean_grade = np.random.uniform(60, 100)
#         variance = 10
#     else:
#         mean_grade = np.random.uniform(0, 100)
#         variance = 20
    
#     grades = np.random.normal(mean_grade, variance, 1)
#     # Clip grades between 0 and 100
#     grades = np.clip(grades, 0, 100)
#     return grades

def quizDist(gpa, status):
    if status == 'Enrolled':
        if 1 - float(quizCompletes[0])*10 < random.choice(range(1,10)):
            mean_grade = quizDistList[1]
            variance = quizDistList[2]
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1                
    else:
        if 1 - float(quizCompletes[1])*10 < random.choice(range(1,10)):
            mean_grade = quizDistList[1]
            variance = quizDistList[2]
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1
            
    return grades

def homeworkDist(gpa, status, row):
    if status == 'Enrolled':   
        if 1 - float(homeworkCompletes[0])*10 < random.choice(range(1,10)):
            if row.name < float(homeworkDistList1[0])*100:
            #if gpa >= 1 - float(homeworkDistList1[0])* 4.0 :
                mean_grade = homeworkDistList1[1]
                variance = homeworkDistList1[2]
            else:
                mean_grade = homeworkDistList2[1]
                variance = homeworkDistList2[2]
            ####################################
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1                
    else:
        if 1 - float(homeworkCompletes[1])*10 < random.choice(range(1,10)):
            if row.name < float(homeworkDistList1[0])*100:
                mean_grade = homeworkDistList1[1]
                variance = homeworkDistList1[2]
            else:
                mean_grade = homeworkDistList2[1]
                variance = homeworkDistList2[2]
            ####################################
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1
            
    return grades

def examDist(gpa, status,row):
    if status == 'Enrolled':
        if 1 - float(examCompletes[0])*10 < random.choice(range(1,10)):
            if row.name < float(examDistList2[0])*100:
                mean_grade = examDistList2[1]
                variance = examDistList2[2]
            elif float(examDistList2[0])*100 <= row.name < float(examDistList2[0])*100 + (examDistList1[0])*100:
                mean_grade = examDistList1[1]
                variance = examDistList1[2]
            else:
                mean_grade = examDistList3[1]
                variance = examDistList3[2]
            ####################################
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1                
    else:
        if 1 - float(examCompletes[1])*10 < random.choice(range(1,10)):
            if row.name < float(examDistList2[0])*100:
                mean_grade = examDistList2[1]
                variance = examDistList2[2]
            elif float(examDistList2[0])*100 <= row.name < float(examDistList2[0])*100 + (examDistList1[0])*100:
                mean_grade = examDistList1[1]
                variance = examDistList1[2]
            else:
                mean_grade = examDistList3[1]
                variance = examDistList3[2]
            ####################################
            grades = np.random.normal(mean_grade, variance)
            # Clip grades between 0 and 100
            grades = np.clip(grades, 0, 100)
        else:
            grades = -1
            
    return grades

#Quiz Frame
quizzes = range(quizDict['count'])
quizframe = pd.DataFrame()
for i in quizzes:
    quizframe['Quiz: ' + str(i+1)] = student_info.apply(lambda row: quizDist(row['GPA'], row['status']),axis=1)

quizframe.set_index(student_ids, inplace=True)
print(quizframe)
quizframe.to_csv('quizframe.csv')

#Homework Frame
homeworks = range(homeworkDict['count'])
homeworkframe = pd.DataFrame()
for i in homeworks:
    homeworkframe['Homework: ' + str(i+1)] = student_info.apply(lambda row: homeworkDist(row['GPA'], row['status'],row),axis=1)
    
homeworkframe.set_index(student_ids, inplace=True)
print(homeworkframe)
homeworkframe.to_csv('homeworkframe.csv')

#Exam Frame
exams = range(examDict['count'])
examframe = pd.DataFrame()
for i in exams:
    examframe['Exam: ' + str(i+1)] = student_info.apply(lambda row: examDist(row['GPA'], row['status'],row),axis=1)

examframe.set_index(student_ids, inplace=True)
print(examframe)    
examframe.to_csv('examframe.csv')

    


