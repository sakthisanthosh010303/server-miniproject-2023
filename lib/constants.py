# Author: Sakthi Santhosh
# Created on: 23/04/2023
EMAIL_BODY = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Alert: Human Intrusion Detected</title>
  </head>
  <body>
    <b>Dear Sir/Madam,</b><br>
    &emsp;Human intrusion was detected by the \"%s\". Details of the incident
    are mentioned below.<br><br>
    <b>Date & Time:</b> %s<br>
    <b>Location:</b> <a href="%s">Google Maps</a><br><br>
    <b>Regrads,</b><br>
    Team Sussy Bakas
  </body>
</html>
"""

SMS_BODY = """Alert: Human Intrusion Detected

Dear Sir/Madam,
    Human intrusion was detected by the \"%s\". Details of the incident are mentioned below.

Date & Time: %s
Location: %s

Regards,
Team Sussy Bakas
"""

SQLITE_DB_URI = "sqlite:///database.db"
LOG_FILE = "./app.log"

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
PREDICTION_THRESHOLD = 0.75
MAPS_LINK = "https://www.google.com/maps/place/"

EMAIL_LIMIT_PERIOD_S = 900
FROM_EMAIL_ID = "sakthisanthosh010303@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
