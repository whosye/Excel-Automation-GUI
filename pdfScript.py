from pypdf import PdfReader

# 1 extract data from part list and compare it from material list - excel sheet 
# 2 Compare connection list with pdf schema
# 2.1 extract data connection list 
# 2.2 exttract data pdf schema 
"""
reader = PdfReader("Pdf/12513810484V01.pdf")


print(len(reader.pages))


page_two = reader.pages[1]

txt = page_two.extract_text()


print(txt)

"""

import pdfplumber



with pdfplumber.open("Pdf/12513810484V01.pdf") as pdf:
    
    for i,page in enumerate(pdf.pages):
        if i ==0:
            print(page.extract_text_simple())
            
            


