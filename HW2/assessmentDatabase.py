import json
import pandas as pd
import random
import numpy as np
import re

student_info = pd.read_csv('student_information.csv')
student_info = student_info.sort_values(by='GPA', ascending=False)
student_info.reset_index(drop=True,inplace=True)

with open("assessment_information.json", 'r') as file:
        dataDict = json.load(file)

assignments = list(dataDict.keys()) 
#print(assignments)


# def gpaSplit(dist):
#     distlen = dist[0]*int(len(student_info))
#     return distlen

def distribution(status, key, row, size, sorted, i):
    
    ####
    ## This theoretically creates the Grades for each student, but right now its not using the multiple distributions
    ## correctly, the bug is it is only using the last distribution for all of the student and not breaking it
    ## up correctly
    ####
    weightEnrolled = dataDict[key]['completes'][0]
    weightDropped = dataDict[key]['completes'][1]
    #distPercentages = list(map(gpaSplit, dataDict[key]['grades']))
    #print(distPercentages)
    
    #print(row.name,type(row))
    if status == 'Enrolled':
        if random.random() < weightEnrolled:
            if row.name < size:
                mean_grade = sorted[i][1]
                #print(mean_grade)
                variance = sorted[i][2]
                grades = random.gauss(mean_grade, variance)
            else:
                return
        else:
            grades = 0
    else:
        #complete = random.choices([True, False], weights=[dataDict[key]['completes'][1],1.0-dataDict[key]['completes'][1]], k=1)[0]
        if random.random() < weightDropped:
            if row.name < size:
                mean_grade = sorted[i][1]
                variance = sorted[i][2]
                grades = random.gauss(mean_grade, variance)
            else:
                return
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
    
    sorted = list(dataDict[key]['grades'])#.sort(key=lambda x: x[1])
    size = 0
    for i in range(len(sorted)):
        size = float(sorted[i][0])*100 + size
        print(size)
        print(sorted[i])
        print(sorted[i][1])
    #frame[columns] = frame.apply(lambda x: distribution(student_info['status',x], key), axis=0)
        for col in columns:
            frame[col] = student_info.apply(lambda row: distribution(row['status'], key, row, size, sorted, i), axis=1)

    #frame[col] = student_info['student_id'].apply(lambda x: x)
    
    print(frame)
    return key

# Use map to iterate over the keys
keys = list(map(process_key, dataDict.keys()))

