import sys
from pathlib import Path
import win32com.client as win32


word_path = r'C:\Users\HPF1COB\Documents\Anaconda\VS code\Outlook meeting\output.docx'
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False
word.DisplayAlerts = False

excel_path = r'C:\Users\HPF1COB\Documents\Anaconda\VS code\Outlook meeting\input.xlsx'
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False
wb = excel.Workbooks.Open(excel_path)
ws = wb.Worksheets(1)
ws.Range("A1:L7").Copy()
wb.Close()


outlook = win32.Dispatch('Outlook.Application')
cal = outlook.CreateItem(1)
cal.Subject = "PSC-Vorbesprechung"
cal.Body = "Hello all"
#cal.Location = "Microsoft Teams Meeting"
cal.Display()
inspector = outlook.ActiveInspector()
word_editor = inspector.WordEditor
word_range = word_editor.Application.ActiveDocument.Content
word_range.PasteExcelTable(False, False, True)
