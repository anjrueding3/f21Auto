import os, PyPDF2, re
from ExcelData import ExcelData

objectList = ExcelData('06/25/15', 40000000, 'UN-JDLKJSFLJ')


#extract PDF text, return as String
def extractPDF_Text(fileName):
    pdfFileObj = open(fileName, 'rb')
    pdf = PyPDF2.PdfFileReader(pdfFileObj)
    firstPage = pdf.getPage(0)
    string = firstPage.extractText()
    return string

#find In house date for forever 21 PO's, returns ihd as string
def findIHD(pdf_text):
    indexOrder = pdf_text.index('(IHD)')
    ihdIndex = indexOrder + 5
    ihd = pdf_text[ihdIndex:ihdIndex + 10]
    return ihd

#find PO number, returns first string in digitString list aka the actual PO number
def findPO(pdf_text):
    fsIndex = pdf_text.index('FSTREND')  #PO num is always 8 numbers before FSTREND in the PDFs
    poIndex = fsIndex - 8
    PO_number = pdf_text[poIndex:fsIndex]
    return PO_number


#find STYLE NUMBER from the pdfs, temporary wrong solution, can't figure this ish out right now
def findStyle(pdf_text):
    endingIndex = pdf_text.index('FSTREND') - 8
    styleIndex = endingIndex - 20
    styleNum = (pdf_text[styleIndex:endingIndex])
    return styleNum

#extract PDF text, find ihd + po + style, put in object, return object
def extractDataToObject(fileName):
    pdfData = extractPDF_Text(fileName)
    ihd = findIHD(pdfData)
    po = findPO(pdfData)
    style = findStyle(pdfData)
    dataObject = ExcelData(ihd, po, style)
    return dataObject

#parse through list of directory files, extract data to object, return list of objects(all required data from directory)
def directory_to_objectList(directory):
    directoryList = os.listdir(directory)
    objectList = []

    for i in range(len(directoryList)):
        if directoryList[i].endswith('.pdf'):
            objectList.append(extractDataToObject(os.path.join(directory, directoryList[i])))
        else:
            print(directoryList[i] + ' is not a pdf file')
            
    return objectList
    

dataList = directory_to_objectList('/Users/andrewding/Desktop/f21PDF')
for object in dataList:
    object.getInfo()


pdfData = extractDataToObject('/Users/andrewding/Desktop/f21PDF/21002111.pdf')
pdfData.getInfo()




