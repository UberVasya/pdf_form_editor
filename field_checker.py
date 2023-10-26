from pypdf import PdfReader

reader = PdfReader("source/template.pdf")
fields = reader.get_form_text_fields()

print(fields)