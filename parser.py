
from docx import Document
from bs4 import BeautifulSoup

def parse_contract_file(file):
    if file.filename.endswith('.docx'):
        return parse_docx(file)
    elif file.filename.endswith('.html'):
        return parse_html(file)
    else:
        return {}

def parse_docx(file):
    doc = Document(file)
    data = {}
    for para in doc.paragraphs:
        if '起始日' in para.text:
            data['start_date'] = para.text.split('：').strip()
        elif '終止日' in para.text:
            data['end_date'] = para.text.split('：').strip()
        elif '月租費' in para.text:
            data['rent'] = para.text.split('：').strip()
    return data

def parse_html(file):
    soup = BeautifulSoup(file, 'html.parser')
    data = {}
    data['start_date'] = soup.find(text='起始日').find_next().text.strip()
    data['end_date'] = soup.find(text='終止日').find_next().text.strip()
    data['rent'] = soup.find(text='月租費').find_next().text.strip()
    return data
