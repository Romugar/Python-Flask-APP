from openpyxl import Workbook

__author__ = "roberto munoz garcia"


class Export(object):

    def __init__(self, datos):
        self.datos = datos


    def export_to_excel(self):
        wb = Workbook()
        wb.save("hola.xlsx")
