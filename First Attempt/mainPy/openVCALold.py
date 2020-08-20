

counter =0
def openVCARDfile(file_path):
    global file2
    file2 = open(file_path, 'rt')


def closeVCARDfile ():
    file2.close()
    print('--------->   VCARD File Closed')

def findNameinFile (dobListFull):
    destFile = open('finalDestFile.vcf', 'at')
    flag = 0
    condition = 0
    i=0
    for line in file2:

        destFile.write(line)
        i=i+1
        if line[:3:] == 'FN:' :
            flag = 1
            fullName = line[3::].split(' ',1)
            print(fullName)
            name = fullName[0]
            print(name)
            if len(fullName)>1:
                lastName = fullName[1]
                lastName = lastName[:-1:]
                print(lastName)
            else:
                lastName = ''
                print('No last name for: ', name)

            for dobLine in dobListFull:
                nameList = dobLine[2][0]
                lastnameList = dobLine[2][1]

                if name == nameList and lastName == lastnameList:
                    print(nameList, ' ', lastnameList,"Name Found for",name,' ',lastName, 'contact')
                    input('press any key to continue...')
                    condition = 1
                    textTobeWritten = 'BDAY:'+dobLine[1][0]+'-'+dobLine[1][1]+'-'+dobLine[1][2]+'\n'
                    print(textTobeWritten)
                    break
                #else:
                    #print('DOB not available')

        if flag == 1 and condition == 1 and line[:4:] == 'TEL;':
            try:
                destFile.write(textTobeWritten)
                print('written at line', i , counter)
                counter= counter +1
                condition = 0
                flag = 0
            except:
                print('Fucked')

    print(nameList[0],'-->',nameList[1])
