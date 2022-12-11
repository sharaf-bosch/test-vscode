import os
import win32com.client as client
from PIL import ImageGrab

workbook_path = r'C:\Users\HPF1COB\Documents\Anaconda\VS code\Outlook meeting\Book1.xlsx'
excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(workbook_path)
sheet = wb.Sheets[0]
excel.visible = 1
copyrange = sheet.Range('A1:O20')
copyrange.CopyPicture(Appearance=1, Format=2)
ImageGrab.grabclipboard().save('paste.png')
excel.quit()

image_path = r'C:\Users\HPF1COB\Documents\Anaconda\VS code\Outlook meeting\paste.png'
html_body = """
    <div>
        <b>Please review the following report and response your feedback....</b><br><br>
    </div>
    <div>
        <img src={}></img>
    </div>
"""

outlook = client.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.To = "p.sharafudheen@in.bosch.com"
message.Subject = "PSC-Vorbesprechung"
message.HTMLBody = html_body.format(image_path)
message.Display()
