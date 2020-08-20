
allvcf= open('goozooFile.vcf', 'at')


tavalod=[3,['1981','08','25'],['Golnaz','Parandeh']]

allvcf.write( 'BEGIN:VCARD' + "\n")
allvcf.write( 'VERSION:3.0' + "\n")
allvcf.write( 'N:' + tavalod[2][1] + ';' + tavalod[2][0] + "\n")
allvcf.write( 'FN:' + tavalod[2][0] + ' ' + tavalod[2][1] + "\n")

if tavalod != '0000':
    allvcf.write('BDAY:' +tavalod[1][0] +'-'+tavalod[1][1]+'-' +tavalod[1][2]+ "\n")
else:
    allvcf.write('BDAY;X-APPLE-OMIT-YEAR=1604:1604-' + tavalod[1][1] + '-' + tavalod[1][2] + "\n")

#allvcf.write( 'ORG:' + 'ATI' + "\n")
#allvcf.write( 'TEL;CELL:' + row[2] + "\n")
#allvcf.write( 'EMAIL:' + row[3] + "\n")
allvcf.write( 'END:VCARD' + "\n")
allvcf.write( "\n")
input('press any key')
allvcf.close()




