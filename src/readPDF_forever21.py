import os, PyPDF2, re

#extract first Page PDF text, return as String
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
    poRegex = re.compile(r'\d\d\d\d\d\d\d\d')
    digitStrings = poRegex.findall(pdf_text)
    return digitStrings[0]



#parse text file for PO, return PO
def extractPO(fileName):
    pdfText = extractPDF_Text(fileName)
    PO = findPO(pdfText)
    return PO

#parse text file for IHD, return ihd
def extractIHD(fileName):
    pdfText = extractPDF_Text(fileName)
    IHD = findIHD(pdfText)
    return IHD

#pass in directory, return dictionary with po and ihd key-value pairs
def extractPoIHD_Dictionary(directory):
    directoryList = os.listdir(directory)
    parsedData = {}
    
    for i in range(len(directoryList)):
        if directoryList[i].endswith('.pdf'):
            parsedData[extractPO(os.path.join(directory, directoryList[i]))] = extractIHD(os.path.join(directory, directoryList[i]))
        else:
            print(directoryList[i] + ' is not a pdf')
    return parsedData

#print formatted dictionary
def printPrettyDictionary(dictionary):
    for key in dictionary:
        print(key + ': ' + dictionary[key])
        



    
#os.path.join(directory, directoryList[i]) = directory + file name
#need to think of potential errors. If mommy adds something wrong to folder.
    
#for i in range(len(directoryList)):
   # parsedData = parsePoIHD(os.path.join(directory, directoryList[i]))



        
