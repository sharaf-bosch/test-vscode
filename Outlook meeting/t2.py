import sys
from pathlib import Path
import win32com.client as win32


excel_path = str(Path.cwd(), 'te.xlsx')
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False
wb = excel.Workbooks.Open(excel_path)
ws = wb.Worksheets(1)
ws.Range("A1:B2").Copy()
wb.Close()

word_path = str(Path.cwd() / 'tw.docx')
word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(word_path)
doc.Content.PasteExcelTable(False, False, True)
doc.Close()

outlook = win32.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.To = "person@email.com"
mail.Subject = "Subject"
# mail.body = "Hello together"
mail.Display()
inspector = outlook.ActiveInspector()
word_editor = inspector.WordEditor
word_range = word_editor.Application.ActiveDocument.Content
word_range.PasteExcelTable(False, False, True)

outlook = win32.gencache.EnsureDispatch('Outlook.Application')
new_mail = outlook.CreateItem(0)
new_mail.To = 'person@email.com'

new_mail.Body = ws.Range("A1:B2").PasteExcelTable(False, False, True)

new_mail.Display()
sys.exit()