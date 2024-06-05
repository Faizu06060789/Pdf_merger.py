import PyPDF2

pdfiles = ["your pdf name", "your pdf name"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)

merger.write('merged.pdf')
merger.close()￼Enter
