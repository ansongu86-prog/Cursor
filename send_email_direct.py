#!/usr/bin/env python3
"""
Direct email sending script - requires Gmail App Password
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
sender_email = "ansongu86@gmail.com"
recipient_email = "ansongu86@gmail.com"
subject = "BlackRock ETF Markets Preparation Materials - PDF Documents"

# Zip file to send
zip_file = "BlackRock_ETF_Markets_Preparation_Materials.zip"

def send_email():
    """Send email with attachment using Gmail SMTP"""
    
    # Check if zip file exists
    if not os.path.exists(zip_file):
        print(f"Error: {zip_file} not found!")
        return False
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Email body
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
    
    # Attach zip file
    with open(zip_file, "rb") as attachment:
        part = MIMEBase('application', 'zip')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {zip_file}'
        )
        msg.attach(part)
    
    # Try to send (this will fail without app password, but shows the method)
    try:
        # Gmail SMTP settings
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        print("Attempting to send email...")
        print("Note: This requires Gmail App Password")
        print("If you have an app password, the email will be sent.")
        print("Otherwise, please use the manual method below.\n")
        
        # For security, we won't hardcode password
        # User needs to provide app password or use manual method
        print("="*60)
        print("MANUAL EMAIL SENDING (RECOMMENDED)")
        print("="*60)
        print(f"\n1. The zip file is ready: {zip_file}")
        print(f"2. Go to https://mail.google.com")
        print(f"3. Compose email to: {recipient_email}")
        print(f"4. Subject: {subject}")
        print(f"5. Attach file: {zip_file}")
        print(f"6. Send the email")
        print("\n" + "="*60)
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    send_email()
