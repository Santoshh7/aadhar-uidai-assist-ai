from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

def summarize_text(text):
    try:
        summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summary error: {e}"
