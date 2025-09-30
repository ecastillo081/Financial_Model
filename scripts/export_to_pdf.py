import win32com.client as win32
# from pathlib import Path
from financial_model.excel_path import excel_path, pdf_path

# excel path
xlsx_path = excel_path

# pdf path
excel = win32.Dispatch("Excel.Application")
excel.Visible = False
wb = excel.Workbooks.Open(str(xlsx_path))

try:
    wb.ExportAsFixedFormat(Type=0, Filename=str(pdf_path))
    print(f"Saved combined PDF: {pdf_path}")
finally:
    wb.Close(SaveChanges=False)
    excel.Quit()
