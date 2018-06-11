from io import BytesIO
from flask import send_file
from openpyxl import Workbook


__author__ = "roberto munoz garcia"


class Export(object):

    def __init__(self, datos):
        self.datos = datos


    def export_to_excel(self):
        wb = Workbook()
        sheet = wb.active  # worksheet
        sheet.title = "Excel Using Openpyxl"
        row = 1
        sheet["A" + str(row)] = "Date"
        sheet["B" + str(row)] = "Hour"
        sheet["C" + str(row)] = "Value"
        filename = "Prueba.xlsx"
        wb.save(filename)

        return send_file(out, mimetype='rgpd-app/vnd.openxmlformats-officedocument.spreadsheetml.sheet', attachment_filename='Prueba.xlsx', as_attachment=True)