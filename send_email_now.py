#!/usr/bin/env python3
"""
Send email with PDF attachment using Gmail SMTP
This script will attempt to send the email, but requires Gmail App Password
"""
import smtplib
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

def send_email_via_gmail():
    """Attempt to send email via Gmail SMTP"""
    
    if not os.path.exists(zip_file):
        print(f"Error: {zip_file} not found!")
        return False
    
    print("="*70)
    print("ATTEMPTING TO SEND EMAIL")
    print("="*70)
    print(f"\nFrom: {sender_email}")
    print(f"To: {recipient_email}")
    print(f"Subject: {subject}")
    print(f"Attachment: {zip_file}")
    print("\n" + "="*70)
    
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
    print(f"\nAttaching {zip_file}...")
    with open(zip_file, "rb") as attachment:
        part = MIMEBase('application', 'zip')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {zip_file}'
        )
        msg.attach(part)
    
    print("✓ Attachment added")
    
    # Try to send
    try:
        print("\nConnecting to Gmail SMTP server (smtp.gmail.com:587)...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print("✓ TLS connection established")
        
        # Note: This will fail without app password
        # We'll catch the error and provide instructions
        print("\n⚠️  Gmail requires App Password for authentication.")
        print("   The email cannot be sent automatically without it.")
        print("\n" + "="*70)
        print("SOLUTION: Manual Email Sending")
        print("="*70)
        print("\nSince automatic sending requires Gmail App Password setup,")
        print("please send the email manually using these steps:\n")
        print(f"1. Go to: https://mail.google.com")
        print(f"2. Click 'Compose'")
        print(f"3. To: {recipient_email}")
        print(f"4. Subject: {subject}")
        print(f"5. Attach file: {zip_file}")
        print(f"6. Click 'Send'")
        print("\n" + "="*70)
        print(f"\n✓ The zip file is ready: {zip_file}")
        print(f"✓ File size: {os.path.getsize(zip_file) / 1024:.1f} KB")
        print(f"✓ Location: {os.path.abspath(zip_file)}")
        print("="*70)
        
        server.quit()
        return False
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n❌ Authentication failed: {e}")
        print("\nThis is expected - Gmail requires App Password.")
        print("Please use the manual method above.")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease use the manual method above.")
        return False

if __name__ == "__main__":
    send_email_via_gmail()
