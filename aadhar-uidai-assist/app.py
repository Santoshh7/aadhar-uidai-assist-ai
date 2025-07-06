

import streamlit as st
import pandas as pd
from grievance_utils import load_complaints
from grievance_classify import classify_complaint
from grievance_summarizer import summarize_text
from grievance_urgency import urgency_score
from fake_detector.aadhaar_utils import run_aadhaar_checks

st.set_page_config(layout="wide", page_title="UIDAI Assist")

st.title("UIDAI Assist — Grievance & Document Intelligence")

module = st.sidebar.selectbox("Choose Module", ["Grievance Categorizer", "Fake Aadhaar Detector"])


if module == "Grievance Categorizer":
    st.header("Aadhaar Grievance Categorizer & Prioritizer")
    file = st.file_uploader("Upload CSV / PDF / JPG / PNG", type=["csv", "pdf", "jpg", "jpeg", "png"])
    manual = st.text_area("Or enter a complaint manually")

    if file or manual:
        try:
            df = load_complaints(file, manual)
            if df is not None and not df.empty:
                results = []
                for i, row in df.iterrows():
                    complaint = row['complaint']
                    category, confidence = classify_complaint(complaint)
                    summary = summarize_text(complaint)
                    urgency = urgency_score(complaint)
                    results.append([i+1, complaint, category, summary, urgency])

                out = st.dataframe(
                    pd.DataFrame(results, columns=["ID", "Complaint", "Category", "Summary", "Urgency"]),
                    use_container_width=True
                )
        except Exception as e:
            st.error(f"❌ {e}")

elif module == "Fake Aadhaar Detector":
    st.header("Fake Aadhaar Detector — Image Forensics")
    aadhaar_file = st.file_uploader("Upload Aadhaar Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    if aadhaar_file:
        with st.spinner("Analyzing image for tampering..."):
            report = run_aadhaar_checks(aadhaar_file)

        st.markdown("### 🔍 Detection Report")
        for key, value in report.items():
            st.markdown(f"- **{key}:** {value}")
            