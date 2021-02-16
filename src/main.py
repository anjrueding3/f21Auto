#! python3

import updateExcel as update
import readPDF_forever21 as read
import sys

directory = sys.argv[1]

parsedData = read.extractPoIHD_Dictionary(directory)

targetExcel = sys.argv[2]

update.updateExcel(targetExcel, parsedData)




