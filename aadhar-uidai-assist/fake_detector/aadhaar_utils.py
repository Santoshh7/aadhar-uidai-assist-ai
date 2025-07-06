import pytesseract
from PIL import Image, ImageChops
from PIL.ExifTags import TAGS
import io
import re

def extract_exif(image):
    """
    Safely extract EXIF metadata from an image if available.
    Works mainly on JPEG or TIFF images.
    """
    try:
        if hasattr(image, "getexif"):
            exif_data = image.getexif()
            return {TAGS.get(tag): value for tag, value in exif_data.items()} if exif_data else {}
    except Exception as e:
        print(f"[EXIF ERROR] {e}")
    return {}

def error_level_analysis(img):
    """
    Perform Error Level Analysis to detect editing.
    Higher max_diff (>20) suggests manipulation.
    """
    resaved = io.BytesIO()
    img.save(resaved, format='JPEG', quality=90)
    resaved.seek(0)
    resaved_img = Image.open(resaved)
    ela_image = ImageChops.difference(img, resaved_img)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    return f"ELA Max Diff: {max_diff} (suspicious if > 20)", max_diff

def run_aadhaar_checks(file):
    """
    Run full Aadhaar image check: OCR, EXIF, and ELA.
    Returns a dictionary report.
    """
    image = Image.open(file).convert("RGB")
    report = {}

    ocr_text = pytesseract.image_to_string(image)
    aadhaar_found = any(re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', line) for line in ocr_text.split('\n'))
    report['OCR Aadhaar Number Format'] = 'Found ✅' if aadhaar_found else 'Not Found ❌'

    exif = extract_exif(image)
    report['EXIF Metadata'] = "Present ✅" if exif else "Missing ❌"

    ela_msg, max_diff = error_level_analysis(image)
    report['ELA Result'] = ela_msg

    confidence = 100
    if not aadhaar_found: confidence -= 30
    if not exif: confidence -= 30
    if max_diff > 20: confidence -= 30

    report['Confidence Score'] = f"{confidence}%"
    report['Final Label'] = "Likely Genuine ✅" if confidence >= 70 else "Tampered ❌"
    return report
