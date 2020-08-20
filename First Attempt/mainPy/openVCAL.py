

# ['January','February','March','April','May','June','July','August','September','October','November','December']:
allNameDOBList = []
monthsDic = {
    'January':'01',
    'February':'02',
    'March':'03',
    'April':'04',
    'May':'05',
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12'
}


def openVCALfile(file_path):
    global file
    file = open(file_path, 'rt')
    populateList(file)


    return allNameDOBList

def closeVCALfile ():
    file.close()
    print('--------->   VCAL File Closed')

def populateList(file):

    allNameDOBList.clear()
    j = 0
    flag = 0

    for line in file:
        j= j+1

        if line[:11:] == 'DESCRIPTION':
            personDOBList = []
            tempDate1 = line [12::]
            tempDate2 = tempDate1.split(' ')

            personDOBList.append(len(tempDate2))

            # Checks to see if the Date of birth is available
            if tempDate2[0] in monthsDic:
                # To replace month with Numbers
                tempDate2[0] = monthsDic[tempDate2[0]]
                # To Fix the date numbers
                temp = tempDate2[1]
                if temp[-2::] == '\\,':
                    tempDate2[1] = temp[:-2:]
                if temp[-3::] == '\\n\n':
                    tempDate2[1] = temp[:-3:]
                if len(tempDate2[1]) ==1:
                    tempDate2[1]= '0'+tempDate2[1]

                # To fix Year numbers and add 0000 if year not available
                if len(tempDate2) == 3 :
                    temp = tempDate2[2]
                    tempDate2[2] = temp[:-1:]
                else:
                    tempDate2.append('0000')

                tempDate3 = [tempDate2[2],tempDate2[0],tempDate2[1]]
                personDOBList.append(tempDate3)
                #print(j, '==> ', personDOBList)
            else:
                personDOBList = [0]
                flag = 1
                #print(j, '==XX><> ', personDOBList)

        if line[:7:] == 'SUMMARY':
            tempName1 = line[8::]
            tempName2 = tempName1[:-12:]

            nameList = tempName2.split(' ', 1)
            personDOBList.append(nameList)

            if flag == 0:
                allNameDOBList.append(personDOBList)
                #print(personDOBList)
                personDOBList = []

        if line[:19:] == 'DTSTART;VALUE=DATE:' and flag == 1:
            #temp = [line[23:25:], line[25:27:], line[19:23:]]
            temp = [line[19:23:], line[23:25:], line[25:27:]]
            #print(temp)
            personDOBList.insert(1,temp)
            allNameDOBList.append(personDOBList)
            flag = 0
            personDOBList = []


