path = "taskList.csv"
path_nameList = 'nameList.txt'
path_kindList = 'kindList.txt'
import csv
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import japanize_matplotlib

def addTaskList(taskClass, taskKind, taskName):
    with open(path, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([taskClass, taskKind, taskName])

def readNameList():
    with open(path_nameList, mode='r', encoding='utf-8') as f:
        nameList = f.read().splitlines()
        return nameList

def readKindList():
    with open(path_kindList, mode='r', encoding='utf-8') as f:
        kindList = f.read().splitlines()
        return kindList

def start(starttime):
    starttime = datetime.datetime.now()

def end(taskClass, taskKind, taskName, starttime):
    endtime = datetime.datetime.now()
    elp = (endtime - starttime).total_seconds()
    date = datetime.date.today()
    with open(path, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, taskClass, taskKind, taskName, starttime.time(), endtime.time(),  elp])

def stringToDate(str):
    spl = str.split('-')
    return datetime.date(int(spl[0]), int(spl[1]), int(spl[2]))

def openData():
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    lstToday = list(filter(lambda x: x[0] == str(datetime.datetime.now().date()), l))
    lstLastOneWeek = list(filter(lambda x: (datetime.date.today() - stringToDate(x[0])).days < 8, l))
    lstLabelsToday = list(map(lambda x: str(x[2]) + ": " + str(x[3]), lstToday))
    lstLabels = list(map(lambda x: str(x[2]) + ": " + str(x[3]), l))
    lstLabelsLastOneWeek = list(map(lambda x: str(x[2]) + ": " + str(x[3]), lstLastOneWeek))
    lstLabelsOrgToday = list(set(lstLabelsToday))
    lstLabelsOrg = list(set(lstLabels))
    lstLabelsOrgLastOneWeek = list(set(lstLabelsLastOneWeek))

    lstTimeToday = []
    lstTime = []
    lstTimeLastOneWeek = []

    for i in lstLabelsOrgToday:
        lstThisLabelToday = list(filter(lambda x: str(x[2]) + ": " + str(x[3]) == i, lstToday))
        timeThisToday = 0.0
        for i in lstThisLabelToday:
            timeThisToday += float(i[6]) / 3600
        lstTimeToday.append(timeThisToday)

    for i in lstLabelsOrg:
        lstThisLabel = list(filter(lambda x: str(x[2]) + ": " + str(x[3]) == i, l))
        timeThis = 0.0
        for i in lstThisLabel:
            timeThis += float(i[6]) / 3600
        lstTime.append(timeThis)

    for i in lstLabelsOrgLastOneWeek:
        lstThisLabelLastOneWeek = list(filter(lambda x: str(x[2]) + ": " + str(x[3]) == i, lstLastOneWeek))
        timeThisLastOneWeek = 0.0
        for i in lstThisLabelLastOneWeek:
            timeThisLastOneWeek += float(i[6]) / 3600
        lstTimeLastOneWeek.append(timeThisLastOneWeek)

    fig = plt.figure()
    plt.rcParams["font.size"] = 8

    ax1 = fig.add_subplot(6,1,1)
    ax2 = fig.add_subplot(6,1,5)
    plt.xticks(rotation=90)
    ax3 = fig.add_subplot(6,1,2)
    plt.xticks(rotation=90)

    lstDateMonth = []
    lstTotalTimeMonth = []
    first = datetime.date.today().replace(day=1)
    while True:
        lstDateMonth.append(first)
        first += datetime.timedelta(days=1)
        if first.day == 1:
            break
    
    for i in lstDateMonth:
        lstThisDay = list(filter(lambda x: str(x[0]) == str(i), l))
        totalTime = 0.0
        for k in lstThisDay:
            totalTime += float(k[6])/3600
        lstTotalTimeMonth.append(totalTime)

    
    ax1.pie(lstTimeToday, labels=lstLabelsOrgToday)
    ax2.bar(lstDateMonth, lstTotalTimeMonth)
    ax3.bar(lstLabelsOrgLastOneWeek, lstTimeLastOneWeek)
    plt.show(block=False)

