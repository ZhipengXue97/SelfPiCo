# Extracted from https://stackoverflow.com/questions/11914472/how-to-use-stringio-in-python3
import PyPDF4
import io

pdfFile = open(r'test.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFile)
pageObj = pdfReader.getPage(1)
pagetext = pageObj.extractText()

for line in io.StringIO(pagetext):
    print(line)

