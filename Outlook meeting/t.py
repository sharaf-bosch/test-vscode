import win32com.client


outlook = win32com.client.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.To = "person@email.com"
mail.Subject = "Subject"
# mail.body = "Hello together"
mail.Display()
inspector = outlook.ActiveInspector()
word_editor = inspector.WordEditor
word_range = word_editor.Application.ActiveDocument.Content
word_range.PasteExcelTable(False, False, True)