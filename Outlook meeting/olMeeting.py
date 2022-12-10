import win32com.client as client
outlook = client.Dispatch("outlook.application")


appt = outlook.CreateItem(1)
appt.Start = "2022-12-12 10:00"  # yyyy-MM-dd hh:mm
appt.Subject = "PSC  -Vorbesprechung"
appt.Body = "Hello Together"
# appt.BodyFormat = HTMLBody
appt.Duration = 60  # In minutes
# appt.Location = "Location Name"
appt.MeetingStatus = 1
appt.Recipients.Add("p.sharafudheen@in.bosch.com")
appt.display()
