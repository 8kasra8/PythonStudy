import makeCal


dataName = {}
lineCounter = 0
flag = 0
fin = open('BALmain.txt', 'rt')
for line in fin:
    #print(type(line))
    lineCounter = lineCounter + 1

    if line == '<div class=\"reminder_data\">\n':
        #print (lineCounter)
        print ('\n')
        lineCounter = 0
        flag = 1
    if lineCounter == 3 and flag == 1 :
        tempName = line[:len(line)-1:]
        print (tempName)
        dataName[tempName] = ''
    if lineCounter == 8 and flag == 1 :
        dataName[tempName] = line.split(' <span')[0]
        print (dataName[tempName])
        flag = 0
        lineCounter = 0


fin.close()
print (dataName)
makeCal.add_to_cal(dataName)
