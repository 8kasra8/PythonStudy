

global counter
def openVCARDfile(file_path):
    global file2
    file2 = open(file_path, 'rt')


def closeVCARDfile ():
    file2.close()
    print('--------->   VCARD File Closed')

def findNameinFile (dobListFull):
    destFile = open('finalDestFile.vcf', 'at')
    counter =1
    i=0
    for line in file2:

        destFile.write(line)
        i=i+1
        if line[:3:] == 'FN:' :

            fullName = line[3::].split(' ',1)
            name = fullName[0]
            if len(fullName)>1:
                lastName = fullName[1]
                lastName = lastName[:-1:]

            else:
                lastName = ''
                print('No last name for: ', name)

            for dobLine in dobListFull:
                nameList = dobLine[2][0]
                lastnameList = dobLine[2][1]

                if name == nameList and lastName == lastnameList:
                    print(nameList, ' ', lastnameList,"Name Found for",name,' ',lastName, 'contact')
                    #input('press any key to continue...')
                    condition = 1
                    if dobLine[1][0] != '0000':
                        textTobeWritten = 'BDAY:'+dobLine[1][0]+'-'+dobLine[1][1]+'-'+dobLine[1][2]+'\n'
                        print(textTobeWritten)
                    else:
                        textTobeWritten = 'BDAY;X-APPLE-OMIT-YEAR=1604:1604-' + dobLine[1][1] + '-' + dobLine[1][2] + '\n'
                        print(textTobeWritten)
                    try:
                        destFile.write(textTobeWritten)
                        print('written at line', i, counter)
                        counter = counter + 1
                        print('deleting ...', dobLine)
                        try:
                             dobListFull.remove(dobLine)
                        except Exception as gooz:
                            print(gooz,'Happend')
                    except Exception as baghali:
                        print('Fucked by:', baghali)
                    break
                #else:
                    #print('DOB not available')

    destFile.close()
    addContact(dobListFull)


def addContact (contactList):

    m=1
    for ingoo in contactList:
        print(ingoo, '-->', m)
        m = m+1

    input('press any key to start writing')
    contactFile = open('newContactsFile.vcf', 'at')
    n = 1
    for long in contactList:
        print(long, n)
        contactFile.write('BEGIN:VCARD' + "\n")
        contactFile.write('VERSION:3.0' + "\n")
        contactFile.write('N:' + long[2][1] + ';' + long[2][0] + "\n")
        contactFile.write('FN:' + long[2][0] + ' ' + long[2][1] + "\n")

        if long[1][0] != '0000':
            contactFile.write('BDAY:' + long[1][0] + '-' + long[1][1] + '-' + long[1][2] + "\n")
        else:
            contactFile.write('BDAY;X-APPLE-OMIT-YEAR=1604:1604-' + long[1][1] + '-' + long[1][2] + "\n")

        contactFile.write('END:VCARD' + "\n")
        contactFile.write("\n")
        n = n + 1


    contactFile.close()


