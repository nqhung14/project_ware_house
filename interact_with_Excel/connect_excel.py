import openpyxl
from openpyxl import Workbook, load_workbook


workbook_obj = load_workbook('Warehouse.xlsx')
# product_list = workbook_obj['Sheet1']
sheet_obj = workbook_obj.active


sheet_obj["A2"] = "hung1"
workbook_obj.save('WareHouse_1.xlsx')




