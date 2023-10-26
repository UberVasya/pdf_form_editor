from pypdf import PdfReader, PdfWriter
import json


class FieldChecker:
    def __init__(self, file: str):
        self.file = file

    def get_fields(self):
        reader = PdfReader(self.file)
        fields = reader.get_form_text_fields()
        return fields


class FieldReplacer:
    def __init__(self, file: str, data: dict = None, template: dict = None):
        if data is None:
            data = {}
        if template is None:
            template = {}
        self.data_json = None
        self.file = file
        self.data = data

    def set_fields(self):
        reader = PdfReader(self.file)
        writer = PdfWriter()
        count_pages = len(reader.pages)
        page = reader.pages[0]
        writer.append(reader)

        return count_pages

    def json_to_dict(self):
        self.data = json.loads(self.data_json)
        return


zyu = FieldChecker('source/template.pdf')
print(zyu.get_fields())
print(type(zyu.get_fields()))

anytext = FieldReplacer('source/template.pdf')
print(anytext.set_fields())

templ = {
    'company': 'company_field',
    'address': 'address_field',
    'address2': 'address_field2'
}
