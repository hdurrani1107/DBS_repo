import json
import pandas as pd
import random
import numpy as np
import re
from operator import itemgetter

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
            grades = 0
    else:
        if random.random() < weightDropped:
                mean_grade = sortedDists[i][1]
                variance = sortedDists[i][2]
                grades = random.gauss(mean_grade, variance)
                grades = np.clip(grades, lbound, ubound)
        else:
            grades = 0
            
    return grades                

def process_key(key):
    ####
    ## Using this function to go through the assignment categories and create a dataframe for each
    ####
    count = int(dataDict[key]['count'])
    columns = list(map(lambda x: f"{key} {x+1}", range(count)))
    frame = pd.DataFrame(index=student_info.index, columns=columns)
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
        
    print(frame)
    frame.to_csv(f'{key}frame.csv')
    return key

# Use map to iterate over the keys
keys = list(map(process_key, dataDict.keys()))

