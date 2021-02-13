from openpyxl import Workbook, load_workbook

workbook = load_workbook('/Users/andrewding/Desktop/poIHDTarget.xlsx')
sheet = workbook.active
    
parsedData = {'20012207': '06/25/2020',
              '21002809': '07/05/2021', '21008188': '07/08/2021', '21002111': '06/01/2021',
              '21008190': '07/08/2021', '21002046': '06/21/2021', '21002546': '06/18/2021'}

maxRow = sheet.max_row
    

for key in parsedData:

    matchFound = False
  
    for i in range(maxRow):
        actualCell = i + 1
        actualPO = 'A' + str(actualCell)
        actualIHD = 'B' + str(actualCell)

        if int(key) == sheet[actualPO].value:
            sheet[actualIHD] = parsedData[key]
            matchFound = True
            break

    if matchFound == False:
        nextEmptyCellNum = maxRow + 1
        emptyPO = 'A' + str(nextEmptyCellNum)
        emptyIHD = 'B' + str(nextEmptyCellNum)
        sheet[emptyPO] = int(key)
        sheet[emptyIHD] = parsedData[key]
        maxRow += 1
    

workbook.save(filename='/Users/andrewding/Desktop/poIHDTarget.xlsx')



    
   # if int(key) == sheet['A2'].value:
        #print(key + ' ' + str(sheet['A2'].value))
