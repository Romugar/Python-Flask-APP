from http.client import HTTPResponse
from openpyxl import Workbook


__author__ = "roberto munoz garcia"


class Export(object):

    def __init__(self, datos):
        self.datos = datos


    def export_to_excel(self):
        output = HttpResponse(mimetype='application/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file_name = "Test.xlsx"
        output['Content-Disposition'] = 'attachment; filename=' + file_name

        wb = Workbook()

        ws = wb.worksheets[0]

        ws.cell('A1').value = 3.14

        wb.save(output)

        return output
