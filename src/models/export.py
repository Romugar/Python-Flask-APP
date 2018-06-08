import io
from flask import send_file
from openpyxl import Workbook


__author__ = "roberto munoz garcia"


class Export(object):

    def __init__(self, datos):
        self.datos = datos


    def export_to_excel(self):
        wb = Workbook()
        ws = wb.active  # worksheet
        ws.title = "Excel Using Openpyxl"
        c = ws.cell(row=5, column=5)
        c.value = "Hi on 5,5"
        out = io.StringIO()
        wb.save(out)
        out.seek(0)

        return send_file(out, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', attachment_filename='xxl.xlsx', as_attachment=True)