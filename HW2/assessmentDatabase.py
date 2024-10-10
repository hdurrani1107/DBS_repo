import json
import pandas as pd
import random
import numpy as np
import re
from operator import itemgetter
import matplotlib.pyplot as plt

student_info = pd.read_csv('student_information.csv')
student_info = student_info.sort_values(by='GPA', ascending=False)
student_info.reset_index(drop=True,inplace=True)

with open("assessment_information.json", 'r') as file:
        dataDict = json.load(file)

assignments = list(dataDict.keys()) 

def distribution(status, key, row, size, sortedDists, i):
    
    ####
    ## This theoretically creates the Grades for each student, but right now its not using the multiple distributions
    ## correctly, the bug is it is only using the last distribution for all of the student and not breaking it
    ## up correctly
    ####
    weightEnrolled = dataDict[key]['completes'][0]
    weightDropped = dataDict[key]['completes'][1]
    lbound = dataDict[key]['range'][0]
    ubound = dataDict[key]['range'][1]

    if status == 'Enrolled':
        if random.random() < weightEnrolled:
                mean_grade = sortedDists[i][1]
                variance = sortedDists[i][2]
                grades = random.gauss(mean_grade, variance)
                grades = np.clip(grades, lbound, ubound)
        else:
            grades = np.nan
    else:
        if random.random() < weightDropped:
                mean_grade = sortedDists[i][1]
                variance = sortedDists[i][2]
                grades = random.gauss(mean_grade, variance)
                grades = np.clip(grades, lbound, ubound)
        else:
            grades = np.nan
            
    return grades                

def process_key(key):
    ####
    ## Using this function to go through the assignment categories and create a dataframe for each
    ####
    count = int(dataDict[key]['count'])
    columns = list(map(lambda x: f"{key} {x+1}", range(count)))
    frame = pd.DataFrame(index=student_info.index, columns=columns)
    score = pd.DataFrame()
    tempFrame2 = pd.DataFrame(index=student_info.index, columns=columns)
    
    dists = list(dataDict[key]['grades'])
    sortedDists = sorted(dists, key=itemgetter(1),reverse=True)
    size = [0,0]
    
    for i in range(len(sortedDists)):
        size = [size[1],size[1] + int(float(sortedDists[i][0])*100)]
        tempFrame = student_info.iloc[size[0]:size[1]]

        for col in columns:
            tempFrame2[col] = tempFrame.apply(lambda row: distribution(row['status'], key, row, size[1], sortedDists, i), axis=1)

        frame = frame.combine_first(tempFrame2)
        frame.set_index(student_info['student_id'])
        
    #print(frame)
    #print( type(dataDict[key]['total']))
    
    if type(dataDict[key]['total']) == int:
        totList = [dataDict[key]['total']]
    else:
        totList = dataDict[key]['total']
        
    for i in range(len(totList)):
        if len(totList) < 2:
            frame[f'{key} Score'] = frame.sum(axis=1)
            frame['Max Score'] = count*100
            score[f'{key} Score'] = frame[f'{key} Score'] / frame['Max Score']
        else:
            score[f"{key} {i+1} Score"] = (
                frame[f"{key} {i+1}"] / 100 )
        #print(score)
        
    frame.to_csv(f'{key}frame.csv')
    return score

# Use map to iterate over the keys
keys = list(map(process_key, dataDict.keys()))

quizscore = keys[0]
print(quizscore)
homeworkscore = keys[1]
print(homeworkscore)
examscore = keys[2]
print(examscore)

# quizweight = quizDict['total']
# quizweight = quizweight/100
# homeworkweight = homeworkDict['total']
# homeworkweight = homeworkweight/100
# examweight = examDict['total']

weights = pd.Series({"Exam 1 Score": 0.1, "Exam 2 Score": 0.2, 
                     "Exam 3 Score": 0.25,"Quiz Score": dataDict['quiz']['total'],
                     "Homework Score": dataDict['homework']['total'],})
final_grade = pd.DataFrame(student_info['student_ids'])
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
plt.scatter(final_gpa['GPA'], student_info['GPA'])
plt.xlabel("Course GPA")
plt.ylabel("Incoming GPA")
plt.title("Scatter Plot")
final_grade.to_csv('student_grades.csv')