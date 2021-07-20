import csv
from datetime import datetime
import codecs
import json

def simplifyCSV(f, e):
    csv_reader = csv.reader(codecs.open(f, 'rU', 'utf-16'), delimiter = '\t')
    next(csv_reader)  # won't print first row
    newlist = []
    studentDetails = []
    tempusnList = []
    for row in csv_reader:
        tempusnList.append(row[0])
        newlist.append(row)
    tempusnList = list(set(tempusnList))
    sortedUSN = sorted(tempusnList)

    for usn in sortedUSN:
        tempData = []
        for studentDetail in newlist:
            if usn == studentDetail[0]:
                tempData.append(studentDetail)
        tempjoined = []
        templeft = []
        for data in tempData:
            if data[1] == 'Left':
                templeft.append(data[2].split(', ')[1][:7])
            else:
                tempjoined.append(data[2].split(', ')[1][:7])
        tempDict = dict({'USN': usn, 'joined': tempjoined, 'left': templeft})
        studentDetails.append(tempDict)
    if e=='':
        estimatedEndTime = int((studentDetails[len(studentDetails) // 2]['joined'][0]).split(':')[0].strip())+1
        dle = f'{estimatedEndTime}:00:00'
    else:
        estimatedEndTime = e
        dle = e
    FMT = '%H:%M:%S'
    dfile = f'simplified-{f[:8]}.csv'
    with open(dfile, mode='w') as finalFile:
        finalWriter = csv.writer(finalFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        finalWriter.writerow(['USN', 'times joined', 'Total Duration'])
        for x in studentDetails:
            tsum = datetime.strptime('00:00:00', FMT) - datetime.strptime('00:00:00', FMT)
            if len(x['joined']) == len(x['left']):
                for i in range(len(x['joined'])):
                    dl = x['left'][i]
                    dj = x['joined'][i]
                    tdelta = datetime.strptime(dl, FMT) - datetime.strptime(dj, FMT)
                    tsum = tsum + tdelta
            else:
                for i in range(len(x['left'])):
                    dl = x['left'][i]
                    dj = x['joined'][i]
                    tdelta = datetime.strptime(dl, FMT) - datetime.strptime(dj, FMT)
                    tsum = tsum + tdelta
                dj = x['joined'][len(x['joined'])-1]
                tdelta = datetime.strptime(dle, FMT) - datetime.strptime(dj, FMT)
                tsum = tsum + tdelta
            finalWriter.writerow([x['USN'], len(x['joined']), tsum])

    return dfile
