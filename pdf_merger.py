from PyPDF2 import PdfWriter
merger = PdfWriter()

pdfs=[]
for pdf in pdfs:
    merger.appends(pdf)

merger.write("Merge")