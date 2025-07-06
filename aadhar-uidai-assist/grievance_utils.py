
import pandas as pd
import pytesseract
import pdfplumber
from PIL import Image
import re

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return clean_text("\n".join([page.extract_text() for page in pdf.pages if page.extract_text()]))

def extract_text_from_image(file):
    image = Image.open(file).convert("RGB")
    return clean_text(pytesseract.image_to_string(image))

def load_complaints(file=None, manual_text=None):
    if file:
        ext = file.name.lower()
        if ext.endswith(".csv"):
            df = pd.read_csv(file)
            df['complaint'] = df['complaint'].astype(str).apply(clean_text)
            return df
        elif ext.endswith(".pdf"):
            return pd.DataFrame({"complaint": [extract_text_from_pdf(file)]})
        elif ext.endswith((".jpg", ".jpeg", ".png")):
            return pd.DataFrame({"complaint": [extract_text_from_image(file)]})
    elif manual_text:
        return pd.DataFrame({"complaint": [clean_text(manual_text)]})
    return None