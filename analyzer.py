from ocr_engine import ocr_from_image
from gemini_ai import analyze_medicine_details

def analyze_medicine_packet(image_path: str) -> str:
    ocr_text = ocr_from_image(image_path)
    if not ocr_text:
        return "No text detected from image."
    
    try:
        print("[DEBUG] OCR Text:", ocr_text)  # You should see this in terminal
        result = analyze_medicine_details(ocr_text)
        return result or "No result from Gemini."
    except Exception as e:
        return f"Error analyzing with Gemini: {str(e)}"
