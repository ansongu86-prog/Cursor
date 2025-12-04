#!/usr/bin/env python3
"""Quick send script - paste your Gmail App Password when prompted"""
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

sender = "ansongu86@gmail.com"
recipient = "ansongu86@gmail.com"
zip_file = "BlackRock_ETF_Markets_Preparation_Materials.zip"

print("="*60)
print("Gmail Email Sender")
print("="*60)
print("\nThis script will send the PDF zip file to your email.")
print("You need a Gmail App Password (not your regular password).")
print("\nGet App Password: https://myaccount.google.com/apppasswords")
print("="*60)

app_password = getpass.getpass("\nEnter your Gmail App Password: ")

if not os.path.exists(zip_file):
    print(f"Error: {zip_file} not found!")
    exit(1)

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = "BlackRock ETF Markets Preparation Materials - PDF Documents"

body = """Dear Recipient,

Please find attached the complete set of BlackRock ETF Markets APAC preparation materials in PDF format.

The package includes:
1. README_Preparation_Materials.pdf - Overview and navigation guide
2. BlackRock_ETF_Markets_Preparation_Guide.pdf - Comprehensive preparation guide  
3. Practice_Projects_Detailed.pdf - 5 detailed practice projects
4. Interview_Questions_Bank.pdf - 17 interview questions with answer frameworks
5. Skill_Assessment_Checklist.pdf - Skills assessment tool
6. Daily_Learning_Plan_Template.pdf - Daily learning plan template

All documents are ready for your preparation journey.

Best regards,
Preparation Materials Generator
"""

msg.attach(MIMEText(body, 'plain'))

with open(zip_file, "rb") as f:
    part = MIMEBase('application', 'zip')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {zip_file}')
    msg.attach(part)

try:
    print("\nConnecting to Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Logging in...")
    server.login(sender, app_password)
    print("Sending email...")
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    print(f"\n✓ Email successfully sent to {recipient}!")
    print(f"✓ Check your inbox for the attachment.")
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nPlease check:")
    print("1. App Password is correct (16 characters, no spaces)")
    print("2. 2-factor authentication is enabled")
    print("3. Internet connection is working")
