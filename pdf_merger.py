import PyPDF2 as pdf

# Open the two PDF files you want to merge
pdf_file1 = 'sample.pdf'
pdf_file2 = 'sample2.pdf'

# Create PdfReader objects for both files
pdf_reader1 = pdf.PdfReader(pdf_file1)
pdf_reader2 = pdf.PdfReader(pdf_file2)

# Create a PdfWriter object for the merged PDF
pdf_writer = pdf.PdfWriter()

# Append pages from the first PDF
for page in pdf_reader1.pages:
    pdf_writer.add_page(page)

# Append pages from the second PDF
for page in pdf_reader2.pages:
    pdf_writer.add_page(page)

# Create a new PDF file to store the merged content
with open('merged2.pdf', 'wb') as merged_pdf:
    pdf_writer.write(merged_pdf)



# pdf_files = ['sample.pdf', 'sample2.pdf']
#
# merger = pdf.PdfMerger()
#
# for filename in pdf_files:
#     pdf_File = open(filename, 'rb')
#     pdf_Reader = pdf.PdfReader(pdf_File)
#     merger.append(pdf_Reader)
#
# pdf_File.close()
#
# merger.write('merged.pdf')
