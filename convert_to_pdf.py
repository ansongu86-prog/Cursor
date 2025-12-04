#!/usr/bin/env python3
"""
Convert Markdown files to PDF using markdown and weasyprint
"""
import os
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# List of markdown files to convert
markdown_files = [
    "README_Preparation_Materials.md",
    "BlackRock_ETF_Markets_Preparation_Guide.md",
    "Practice_Projects_Detailed.md",
    "Interview_Questions_Bank.md",
    "Skill_Assessment_Checklist.md",
    "Daily_Learning_Plan_Template.md"
]

# CSS for better PDF formatting
css_style = """
@page {
    size: A4;
    margin: 2cm;
}
body {
    font-family: 'Arial', 'Helvetica', sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
}
h1 {
    font-size: 24pt;
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
    margin-top: 30px;
    margin-bottom: 20px;
}
h2 {
    font-size: 18pt;
    color: #34495e;
    margin-top: 25px;
    margin-bottom: 15px;
    border-bottom: 1px solid #bdc3c7;
    padding-bottom: 5px;
}
h3 {
    font-size: 14pt;
    color: #555;
    margin-top: 20px;
    margin-bottom: 10px;
}
h4 {
    font-size: 12pt;
    color: #666;
    margin-top: 15px;
    margin-bottom: 8px;
}
code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 10pt;
}
pre {
    background-color: #f8f8f8;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    overflow-x: auto;
    font-size: 9pt;
}
pre code {
    background-color: transparent;
    padding: 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 15px 0;
    font-size: 10pt;
}
table th, table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
table th {
    background-color: #3498db;
    color: white;
    font-weight: bold;
}
table tr:nth-child(even) {
    background-color: #f2f2f2;
}
ul, ol {
    margin: 10px 0;
    padding-left: 30px;
}
li {
    margin: 5px 0;
}
blockquote {
    border-left: 4px solid #3498db;
    margin: 15px 0;
    padding-left: 15px;
    color: #666;
    font-style: italic;
}
a {
    color: #3498db;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
hr {
    border: none;
    border-top: 2px solid #ecf0f1;
    margin: 20px 0;
}
"""

def markdown_to_pdf(md_file, output_pdf):
    """Convert a markdown file to PDF"""
    print(f"Converting {md_file} to {output_pdf}...")
    
    # Read markdown file
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: {md_file} not found!")
        return False
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'tables', 'toc']
    )
    
    # Wrap in HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{Path(md_file).stem}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    try:
        HTML(string=full_html).write_pdf(
            output_pdf,
            stylesheets=[CSS(string=css_style)]
        )
        print(f"✓ Successfully created {output_pdf}")
        return True
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def main():
    """Main function to convert all markdown files"""
    print("Starting PDF conversion...")
    print("=" * 50)
    
    success_count = 0
    pdf_files = []
    
    for md_file in markdown_files:
        if os.path.exists(md_file):
            pdf_file = md_file.replace('.md', '.pdf')
            if markdown_to_pdf(md_file, pdf_file):
                success_count += 1
                pdf_files.append(pdf_file)
        else:
            print(f"Warning: {md_file} not found, skipping...")
    
    print("=" * 50)
    print(f"Conversion complete! {success_count}/{len(markdown_files)} files converted.")
    print("\nGenerated PDF files:")
    for pdf in pdf_files:
        print(f"  - {pdf}")
    
    return pdf_files

if __name__ == "__main__":
    pdf_files = main()
