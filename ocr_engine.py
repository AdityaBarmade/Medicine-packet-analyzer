import easyocr
import cv2
from PIL import Image
import pytesseract

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def ocr_from_image(image_path):
    # Using EasyOCR to extract text
    result = reader.readtext(image_path)
    
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + "\n"

    return extracted_text

def ocr_from_image_tesseract(image_path):
    # Using Tesseract to extract text
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text
