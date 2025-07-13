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
##Project Structure

<pre> 📁 uidai-grievance-assist/ ├── 📄 app.py → Main Streamlit Interface (UI + Module Selector) ├── 📄 grievance_utils.py → File handling, OCR parsing (CSV, PDF, Image) ├── 📄 grievance_classify.py → Complaint classification via BART (zero-shot) ├── 📄 grievance_summarizer.py → Summarizes complaints using BART CNN ├── 📄 grievance_urgency.py → Urgency detection using emotion + sentiment ├── 📁 fake_detector/ → Aadhaar forgery detection module │ └── 📄 aadhaar_utils.py → Image tampering logic, layout checks ├── 📄 requirements.txt → All external dependencies └── 📄 README.md → Full documentation with warnings, usage, credits </pre>

## 🖼️ Live Demo & Interface Screenshots

Get a quick look at how **UIDAI Assist** helps users seamlessly interact with Aadhaar services.

🏠 1. Home Interface – Module Selection
The landing screen allows users to select from two core modules — Grievance Categorizer and Fake Aadhaar Detector — to begin the desired Aadhaar-related service.

<img width="1920" height="1020" alt="Screenshot 2025-07-06 205327" src="https://github.com/user-attachments/assets/8d0bcd4d-9dd6-4b7e-9212-74ce1d50cdf0" />


📁 2. Grievance Categorizer — Upload CSV
<img width="1920" height="1020" alt="Screenshot 2025-07-06 205840" src="https://github.com/user-attachments/assets/47f4c4e0-10f0-4db1-a1ed-9e908cae6d0b" />
<img width="550" height="300" alt="Screenshot 2025-07-06 210525" src="https://github.com/user-attachments/assets/5b76c29a-0583-4645-a105-3769cbc7cdc6" />
<img width="500" height="300" alt="Screenshot 2025-07-06 210538" src="https://github.com/user-attachments/assets/09d544e5-8b61-4d5f-9219-61f33546f6e3" />
<img width="500" height="300" alt="Screenshot 2025-07-06 210548" src="https://github.com/user-attachments/assets/852abb7d-2b6f-4a60-bc30-9b80b603806e" />

Users can upload complaint datasets in .CSV format. The system processes each entry, categorizes the grievance type, and assigns a priority score for streamlined resolution.

📄 3. Grievance Categorizer — Upload PDF
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210039" src="https://github.com/user-attachments/assets/e4e9e824-f6ee-495a-8f0e-7fe8ddf2c092" />
For document-based submissions, users can upload Aadhaar complaint letters in .PDF format. The NLP engine extracts and analyzes content for automated classification.


🖼️ 4. Grievance Categorizer — Upload PNG/JPG
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210134" src="https://github.com/user-attachments/assets/88ba7fc3-631e-44b8-ad9a-e23e92723161" />
Complaints submitted as scanned images (JPG/PNG) are processed using OCR and NLP to extract relevant text, identify grievance types, and set urgency levels.

🖼️ 5. Grievance Categorizer — Enter Complaint Manually
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210742" src="https://github.com/user-attachments/assets/a63b1f38-e85a-4cb6-92fd-7ec70fa89e84" />


🔍 Fake Aadhaar Detector — Image Forensics
This module helps verify the authenticity of uploaded Aadhaar card images using advanced forensics like OCR validation, metadata checks, and Error Level Analysis (ELA). It generates a detailed report highlighting anomalies and assigning a tampering confidence score.

🧭 Module Interface — Aadhaar Forgery Detection
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210817" src="https://github.com/user-attachments/assets/720af524-4d02-45b5-be7d-c20d525b1c2d" />
Users can upload .JPG, .JPEG, or .PNG images of Aadhaar cards. The system scans the image, applies forensic techniques, and generates a real-time Detection Report indicating whether the document is genuine or tampered.

🧪 Test Case 1 — Dummy Document (Tampered)

<img width="1920" height="1020" alt="Screenshot 2025-07-06 210847" src="https://github.com/user-attachments/assets/2b7fff4e-66cc-408c-93c8-f86635f799b2" />
The uploaded image was a completely fake Aadhaar structure. The system flagged the following:

❌ Aadhaar Number Format: Not detected via OCR

❌ EXIF Metadata: Missing

❌ ELA Score: 70 (very high)

🔻 Confidence Score: 10%

❌ Final Label: Tampered

✅ Test Case 2 — Valid Format Only (Suspicious)
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210913" src="https://github.com/user-attachments/assets/869910e8-6222-44d7-b8e9-7c87628eff01" />

This Aadhaar image had a valid EXIF Metadata but failed in other verification aspects:

❌ OCR: Detected incorrect Aadhaar number format

✅ EXIF Metadata: Present

⚠️ ELA Score: Moderate (around 45) (suspicious if >20)

⚠️ Confidence Score: ~40%

❌ Final Label: Suspicious / Possibly Tampered


🟢 Test Case 3 — Genuine Aadhaar Detected
<img width="1920" height="1020" alt="Screenshot 2025-07-06 210928" src="https://github.com/user-attachments/assets/258f3d3d-0d32-48a5-8350-5f2d873587c9" />

The uploaded Aadhaar card was authentic. All checks passed:

✅ OCR: Aadhaar number format detected

✅ EXIF Metadata: Present

✅ ELA Score: 15 (well below tampering threshold)

🔼 Confidence Score: 100%

✅ Final Label: Genuine






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

Passionate about building AI-driven solutions for public infrastructure and digital identity security.
