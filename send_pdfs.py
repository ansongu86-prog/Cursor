#!/usr/bin/env python3
"""
Send PDF files via email
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import zipfile

# Email configuration
sender_email = "ansongu86@gmail.com"  # Using your email as sender (will need app password)
recipient_email = "ansongu86@gmail.com"
subject = "BlackRock ETF Markets Preparation Materials - PDF Documents"

# PDF files to send
pdf_files = [
    "README_Preparation_Materials.pdf",
    "BlackRock_ETF_Markets_Preparation_Guide.pdf",
    "Practice_Projects_Detailed.pdf",
    "Interview_Questions_Bank.pdf",
    "Skill_Assessment_Checklist.pdf",
    "Daily_Learning_Plan_Template.pdf"
]

def create_zip_archive():
    """Create a zip file with all PDFs"""
    zip_filename = "BlackRock_ETF_Markets_Preparation_Materials.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pdf_file in pdf_files:
            if os.path.exists(pdf_file):
                zipf.write(pdf_file)
                print(f"Added {pdf_file} to zip")
    return zip_filename

def send_email_with_attachment(zip_file):
    """Send email with PDF zip attachment"""
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Email body
    body = """
Dear Recipient,

Please find attached the complete set of BlackRock ETF Markets APAC preparation materials in PDF format.

The package includes:
1. README_Preparation_Materials.pdf - Overview and navigation guide
2. BlackRock_ETF_Markets_Preparation_Guide.md - Comprehensive preparation guide
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
    if os.path.exists(zip_file):
        with open(zip_file, "rb") as attachment:
            part = MIMEBase('application', 'zip')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {zip_file}'
            )
            msg.attach(part)
    
    # Try to send via Gmail SMTP
    try:
        # Note: This requires Gmail App Password
        # For security, we'll provide instructions instead
        print("\n" + "="*60)
        print("EMAIL SENDING INSTRUCTIONS")
        print("="*60)
        print("\nTo send the email, you have two options:\n")
        print("OPTION 1: Use Gmail Web Interface")
        print("1. Go to https://mail.google.com")
        print(f"2. Compose new email to {recipient_email}")
        print(f"3. Subject: {subject}")
        print("4. Attach the zip file: BlackRock_ETF_Markets_Preparation_Materials.zip")
        print("5. Send\n")
        
        print("OPTION 2: Use Python script with Gmail App Password")
        print("1. Enable 2-factor authentication on your Gmail account")
        print("2. Generate an App Password: https://myaccount.google.com/apppasswords")
        print("3. Use the script below with your app password\n")
        
        print("The zip file has been created: BlackRock_ETF_Markets_Preparation_Materials.zip")
        print("="*60)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("Creating zip archive...")
    zip_file = create_zip_archive()
    print(f"\n✓ Created {zip_file}")
    
    print("\nPreparing email...")
    send_email_with_attachment(zip_file)
    
    # List all files
    print("\n" + "="*60)
    print("FILES READY:")
    print("="*60)
    print(f"Zip file: {zip_file}")
    print("\nIndividual PDF files:")
    for pdf in pdf_files:
        if os.path.exists(pdf):
            size = os.path.getsize(pdf) / 1024  # Size in KB
            print(f"  - {pdf} ({size:.1f} KB)")

if __name__ == "__main__":
    main()
