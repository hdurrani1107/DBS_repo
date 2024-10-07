import json
import pandas as pd
import random
import numpy as np
import re

dataframe = pd.DataFrame

with open("student_information.json", 'r') as file:
    dataDict = json.load(file)
    
gpaDict = dict(dataDict['GPA'])
statusDict = dict(dataDict['status'])
distParamfull = re.findall(r'\((.*?)\)',gpaDict['dist'])
distParam = re.split(',',distParamfull[0])
distRange = list(gpaDict['range'])
idDict = dict(dataDict['student_id'])
statusList = list(dataDict['status'])

columnsS = list(dataDict)
columnsS = columnsS[1:]
dist = gpaDict['dist']

firstNames = []
lastNames = []
GPAs = []
status = []
student_id = []
status = []

database = pd.DataFrame
database = database(index=range(dataDict['number']),columns=list(columnsS))


##database.apply()
## This way uses the .apply method, to iterate through each row of the dataframe and call the generate_student_data function
## to generate the names, gpas, ect for each row at a time as oppose to the list method, no for loops used here.    
def generate_student_data(row):
    first_name = random.choice(dataDict['first_names'])
    last_name = random.choice(dataDict['last_names'])
    gpa = round(random.gauss(float(distParam[0]), float(distParam[1])), 1)
    student_id = idDict['prefix'] + str(np.random.choice(range(int(idDict['min']), int(idDict['max'])), replace=False))
    statusOdds = random.randrange(1, 10)
    if statusOdds < float(statusList[0][0]) * 10:
        status = statusList[0][1] 
    else:
        statusList[1][1]
        
    return pd.Series([first_name, last_name, gpa, student_id, status])

# Apply the function to each row
database[['first_names', 'last_names', 'GPA', 'student_id', 'status']] = database.apply(generate_student_data, axis=1)
database['GPA'] = database['GPA'].clip(distRange[0], distRange[1])

#######################################################
## This is the old code that used a for loop to generate the student data
## The old way created lists of first names, last names, gpas, ect based on the number of students
## then just put those lists in the dataframe
# for i in range(dataDict['number']):

#     firstNames.append(random.choice(list(dataDict['first_names'])))
#     lastNames.append(random.choice(list(dataDict['last_names'])))
#     GPAs.append(round(random.gauss(float(distParam[0]),float(distParam[1])),1))
#     student_id.append(0)
#     student_id[i] = idDict['prefix'] + str(np.random.choice(range(int(idDict['min']),int(idDict['max'])),replace=False))
#     statusOdds = random.randrange(1,10)
#     if statusOdds < float(statusList[0][0])*10:
#         status.append(statusList[0][1])
#     else:
#         status.append(statusList[1][1])
    
#GPAs = np.clip(GPAs,distRange[0],distRange[1])
# database.first_names = firstNames
# database.last_names = lastNames
# database.GPA = GPAs
# database.student_id = student_id
# database.status = status

#######################################################

print(database)
database.to_csv('student_information.csv')