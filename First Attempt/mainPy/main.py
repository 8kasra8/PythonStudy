import openVCAL
import openVCARD

testobject = openVCAL
resultVCAL = testobject.openVCALfile('testFileVCAL.txt')
testobject.closeVCALfile()

#i=0
#for item in resultVCAL:
    #print(resultVCAL[i],'--->', i+1)

 #   print (resultVCAL[i][1],resultVCAL[i][2])
 #   i = i+1
contactObject = openVCARD
contactObject.openVCARDfile('VCARD123.vcf')
contactObject.findNameinFile(resultVCAL)
contactObject.closeVCARDfile()

