

import csv

with open('MoonAgeLog01.csv','r') as f:
    reader = csv.reader(f)

    pages = []

    for row in reader:
        newLine = row[:8] 

        if(row[8]):
            if(row[9]):
                StartLat = '{:6.3f}'.format(int(row[8])+float(row[9])/60.)
                newLine.append(StartLat)
            else:
                newLine.append('')
        else:
            newLine.append('')

        if(row[10]):
            if(row[11]):
                StartLon = '{:6.3f}'.format(int(row[10])+float(row[11])/60.)
                newLine.append(StartLon)
            else:
                newLine.append('')
        else:
            newLine.append('')

        if(row[12]):
            if(row[13]):
                EndLat = '{:6.3f}'.format(int(row[12])+float(row[13])/60.)
                newLine.append(EndLat)
            else:
                newLine.append('')
        else:
            newLine.append('')

        if(row[14]):
            if(row[15]):
                EndLon = '{:6.3f}'.format(int(row[14])+float(row[15])/60.)
                newLine.append(EndLon)
            else:
                newLine.append('')
        else:
            newLine.append('')

        pages.append(newLine)

with open ('res.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(pages)
