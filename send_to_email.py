#!/usr/bin/env python3
"""
Send PDFs to email - requires Gmail App Password
Usage: 
  GMAIL_APP_PASSWORD=your_password python3 send_to_email.py
  OR
  python3 send_to_email.py your_app_password
"""
import smtplib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuration
sender_email = "ansongu86@gmail.com"
recipient_email = "ansongu86@gmail.com"
subject = "BlackRock ETF Markets Preparation Materials - PDF Documents"
zip_file = "BlackRock_ETF_Markets_Preparation_Materials.zip"

def send_email(app_password):
    """Send email with PDF zip attachment"""
    
    if not os.path.exists(zip_file):
        print(f"Error: {zip_file} not found!")
        return False
    
    try:
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
        
        # Connect to Gmail SMTP server
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("Logging in...")
        server.login(sender_email, app_password)
        
        print("Sending email...")
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"\n✓ Email successfully sent to {recipient_email}!")
        print(f"✓ Attachment: {zip_file}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your Gmail App Password.")
        print("\nTo get a Gmail App Password:")
        print("1. Enable 2-factor authentication on your Gmail account")
        print("2. Go to: https://myaccount.google.com/apppasswords")
        print("3. Generate an app password for 'Mail'")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    # Get app password from environment variable or command line argument
    app_password = os.environ.get('GMAIL_APP_PASSWORD')
    
    if not app_password and len(sys.argv) > 1:
        app_password = sys.argv[1]
    
    if not app_password:
        print("="*70)
        print("GMAIL APP PASSWORD REQUIRED")
        print("="*70)
        print("\nTo send email automatically, you need a Gmail App Password.")
        print("\nOption 1: Set environment variable")
        print("  export GMAIL_APP_PASSWORD=your_app_password")
        print("  python3 send_to_email.py")
        print("\nOption 2: Pass as argument")
        print("  python3 send_to_email.py your_app_password")
        print("\nOption 3: Manual sending (RECOMMENDED)")
        print(f"  1. Go to https://mail.google.com")
        print(f"  2. Compose email to: {recipient_email}")
        print(f"  3. Subject: {subject}")
        print(f"  4. Attach: {zip_file}")
        print(f"  5. Send")
        print("\n" + "="*70)
        print(f"\n✓ All files are ready in the current directory:")
        print(f"  - {zip_file} (contains all PDFs)")
        print("\nTo get Gmail App Password:")
        print("  1. Enable 2FA: https://myaccount.google.com/security")
        print("  2. Generate App Password: https://myaccount.google.com/apppasswords")
        print("="*70)
        return
    
    # Send email
    send_email(app_password)

if __name__ == "__main__":
    main()
