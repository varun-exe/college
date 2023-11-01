from PyPDF2 import PdfWriter, PdfReader

num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('/Users/varun/Downloads/python.pdf', 'rb') #or address of the pdf file(read binary)
pdf2 = open('/Users/varun/Downloads/web.pdf', 'rb')

pdf_writer = PdfWriter()

pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)

pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)

with open('output_file.pdf', 'wb') as output:
    pdf_writer.write(output)

print("Done!")
