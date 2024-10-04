# Copyright 2024 Alex Tianji Sun tianjis@bu.edu
# Copyright 2024 Humzah Durrani hhd8@bu.edu
# Copyright 2024 Stephan Bscheider sbsch@bu.edu
###########################################################################
## Import libraries                                                      ##
###########################################################################
import sys
import os
import datetime
import time
import glob

###########################################################################
## Variable Definitions used in multiple functions                       ##
###########################################################################
cmds = sys.argv
walks = os.walk(os.getcwd())

###########################################################################
## Function Definitions for each searcher argument                       ##
###########################################################################
#Search Date
def dateTime(start, end):
    
    startStamp = time.mktime(start.timetuple())
    endStamp = time.mktime(end.timetuple())
    
    for x in walks:
        for y in x[2]:
            filePath = x[0]+"/"+y
            fileDateStamp = os.path.getmtime(filePath)
            if startStamp <= fileDateStamp and fileDateStamp <= endStamp:
                fileDate = datetime.datetime.fromtimestamp(fileDateStamp)
                print(filePath,fileDate)
    return

#Search full filename
def filename():
    
    cmd = "**/"+cmds[cmds.index("-f") + 1]
    file = glob.glob(cmd,recursive=True)
    print(file)
    if file:
        print("File is in Directory")
    else:
        print("File is not in directory")

#Search File type
def filetype():
    
    if cmds[cmds.index("-t") + 1]:
        cmd = "**/*"+cmds[cmds.index("-t") + 1]
        files = glob.glob(cmd,recursive=True)
        for file in files:
            print(file)
    else:
        print("No file type described please input proper file type. Ex. '*.mp3'")

#Search text
def search_text(directory, text):
    a = False
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if text.lower() in filename.lower():
                print(f"Matching file: {os.path.join(root, filename)}")
                a = True
    if a == False:
        print("No matching files found.")

def readme():
    print("Searcher Function Help:\n")
    print("Type '-t' followed by filetype (ex. .txt or .py) to search directory",
          "\nfor all files with filetype\n",
          "\nType '-f' followed by FILENAME.TYPE to search directory for file\n",
          "\nType '-c' followed by text to search (ex. 'cat' for all files in directory with",
          "\nspecified text and there file location\n",
          "\nType '-d' followed by YYYY-MM-DD:YYYY-MM-DD to search files in directory",
          "\nwithin a specified date. If one set of dates is empty function will",
          "\neither search from the beginning of time till specified date or",
          "\nor from specified date till today and display all files within that range")

###########################################################################
## If statements, to parse args and call functions                       ##
###########################################################################
#Search for file Type
if "-f" in cmds:
    filename()
    
#Type
if "-t" in cmds:
    filetype()
    
#Text to search
if "-c" in cmds:
    target_text = cmds[cmds.index("-c") + 1]
    search_text('.', target_text)
    
#Date search
if "-d" in cmds:
    ## formated as " YYYY-mm-dd:YYYY-mm-dd" ##
    range = cmds[cmds.index("-d") + 1]
    rangeSplit = range.split(":")
    if rangeSplit[0] == "":
        start = datetime.date.min
    else:
        start = datetime.datetime.fromisoformat(rangeSplit[0])
    
    if rangeSplit[1] == "":
        end = datetime.datetime.today()
    else:
        end = datetime.datetime.fromisoformat(rangeSplit[1])
    
    dateTime(start, end)
    
#Help Function
if "-h" in cmds:
    readme()