# UIDAI Assist — Grievance Analyzer & Fake Aadhaar Detector

**UIDAI Assist** is an AI-powered platform designed to automate and enhance the handling of Aadhaar-related grievances and the detection of forged Aadhaar documents. Built using powerful NLP pipelines and image forensics, the system combines **natural language understanding** with **document tampering detection** to simulate a next-gen, secure UIDAI service prototype.

---

## 🚀 Features Overview

### 1️⃣ Grievance Categorizer & Summarizer
> 📋 **Smart Complaint Intelligence Module**

- 🔍 **Multi-format Input**: Accepts CSV, PDF, JPG, PNG, and manual complaint text.
- 🧠 **AI-Based Categorization**: Classifies Aadhaar-related complaints into categories using Zero-Shot Classification.
- ✂️ **Automatic Summarization**: Uses a pre-trained summarizer to generate concise summaries for long complaints.
- ⚠️ **Urgency Detection**: Identifies emotional sentiment and flags urgency (High / Medium / Low) using emotion models and VADER sentiment scoring.

### 2️⃣ Fake Aadhaar Detector
> 🛡️ **Image Forensics-Based Fraud Detection Module**

- 📸 **Upload Aadhaar Image (JPG/PNG)**: Supports real-time image uploads.
- 🔎 **OCR & Layout Parsing**: Extracts text and visual structure using Tesseract and rule-based logic.
- 🚨 **Forgery Checks**: Detects signs of tampering like misaligned text, manipulated zones, and inconsistent fonts.
- 🧾 **Structured Report Generation**: Outputs a clear report highlighting authenticity indicators.

---

## 🧠 Tech Stack

| Layer        | Tools & Libraries                                |
|--------------|--------------------------------------------------|
| Frontend     | Streamlit                                        |
| NLP Models   | Transformers (`facebook/bart-large-cnn`, `facebook/bart-large-mnli`, `distilroberta`) |
| OCR & Image  | Tesseract OCR, Pillow, pdfplumber                |
| Sentiment    | VADER Sentiment Analyzer                         |
| Language     | Python                                           |

---

## ⚙️ Installation Guide

```bash
# Clone the project
git clone https://github.com/your-repo/uidai-grievance-assist.git
cd uidai-grievance-assist

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

uidai-grievance-assist/
├── app.py                        # Main Streamlit Interface
├── grievance_utils.py           # OCR / Text loaders
├── grievance_classify.py        # NLP-based complaint classifier
├── grievance_summarizer.py      # Complaint summarization logic
├── grievance_urgency.py         # Urgency prediction
├── fake_detector/
│   └── aadhaar_utils.py         # Aadhaar forgery analysis
├── requirements.txt
└── README.md


## ⚠️ Caution

> ❗ **This tool is strictly intended for academic, testing, and demonstration purposes only.**
>
> 🚫 **Do NOT upload or test this application with real Aadhaar card images or genuine personal ID information** (yours or anyone else’s).
>
> ⚠️ This application uses **advanced AI models from Hugging Face**, capable of:
> - Extracting embedded information from uploaded images
> - Reading and decoding **QR codes** present on Aadhaar documents
> - Revealing personal identifiable information (PII) from scanned content
>
> 🧠 These models are trained on large datasets and can infer or expose sensitive details automatically.
>
> 🛡️ Uploading actual identity documents **may lead to privacy violations, unintentional data exposure, or legal consequences.**
>
> 👉 Treat all inputs as **mock/demo data only** during usage and testing.
>
> ✅ To safely test the system, a **`sample_data/`** folder has been provided containing **public Aadhaar-like samples** downloaded from open sources via Google Search.  
> Use these demo images only for testing and avoid uploading any personal document.


🛠️ Built to demonstrate secure automation of Aadhaar grievance redressal and document fraud detection for UIDAI-like frameworks.
Combines AI, NLP, and image forensics to improve public-facing governance systems.

**Developed By**: **SANTOSH THAKUR**

##Passionate about building AI-driven solutions for public infrastructure and digital identity security.
