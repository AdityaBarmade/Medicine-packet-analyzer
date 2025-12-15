Medicine Packet Analyzer
Medicine Packet Analyzer is a Python-based desktop application that reads text from medicine packet images and converts it into clear, structured medical information using OCR and an AI model (Google Gemini).
Overview
Medicine packets usually contain critical details such as drug name, dosage, expiry, warnings, and usage instructions, which are often hard to read or understand for non-experts. This project lets users upload an image of a medicine strip or box, extracts text via OCR, and then uses Gemini to generate a patient-friendly explanation of the medicine information.​

Features
Modern PyQt5 GUI to upload medicine images and view results.​

Image preprocessing (resize, grayscale, enhancement) before OCR for better recognition.​

Dual OCR pipeline using EasyOCR (primary) and Tesseract (fallback) to improve accuracy.​

AI-powered summarization with Google Gemini API: usage, warnings, dosage, expiry, alternatives, and more.​

Scrollable, editable result box with copy-to-clipboard and save-to-file options.​

Basic error handling when no text is detected or the AI service fails.​

System Architecture
The project follows a layered architecture to keep components modular and maintainable.​

User Interface Layer (PyQt5): GUI for selecting images, starting analysis, and visualizing results.​

Image Processing Layer (OpenCV & PIL): Cleans and prepares images for OCR.​

OCR Engine Layer (EasyOCR / Tesseract): Extracts raw text from the processed image.​

AI Analysis Layer (Gemini API): Interprets OCR text using an LLM to produce structured summaries.​

Output Rendering Layer (PyQt5): Displays processed information and supports user actions like copy/save.​
Tech Stack
| Component         | Technology / Tool            |
| ----------------- | ---------------------------- |
| Programming       | Python 3.10+                 |
| GUI Framework     | PyQt5                        |
| OCR Engines       | EasyOCR, Tesseract OCR       |
| Image Processing  | OpenCV, Pillow (PIL)         |
| AI / LLM          | Google Gemini API            |
| Config Management | python-dotenv with .env file |
| Environment / IDE | Local Python environment     |
Project Structure
Your repository can be structured as follows (matching your files as closely as possible):
.
├── main.py           # CLI entry point (image path from terminal)
├── gui_app.py        # PyQt5 GUI application
├── analyzer.py       # Connects OCR and Gemini to produce final analysis
├── ocr_engine.py     # OCR logic (EasyOCR + Tesseract)
├── gemini_ai.py      # Gemini API integration and prompt construction
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment configuration
└── README.md

main.py runs OCR + AI from the command line using an image path.​

gui_app.py launches the graphical interface for interactive use.​

ocr_engine.py encapsulates image loading, preprocessing, and OCR calls.​

gemini_ai.py prepares prompts and sends requests to the Gemini model.​

analyzer.py ties OCR and AI together into a single analyze_medicine_packet function.​

Installation
1. Clone the repository
git clone https://github.com/AdityaBarmade/Medicine-packet-analyzer.git
cd Medicine-packet-analyzer
2. Create and activate a virtual environment 
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
3. Install dependencies
requirements.txt should include at least: easyocr, opencv-python, pillow, pytesseract, PyQt5, python-dotenv, requests
pip install -r requirements.txt
4. Configure the Gemini API key
GEMINI_API_KEY=your_gemini_api_key_here
The key is loaded using python-dotenv so you do not need to hardcode it in gemini_ai.py.​
Usage
CLI Mode
Run analysis from the terminal with an image path:

bash
python main.py path/to/medicine_image.jpg
This prints the AI-generated analysis in the console.​

GUI Mode
Launch the desktop GUI:

bash
python gui_app.py
Then:

Click Browse Image and choose a .jpg, .jpeg, or .png file of a medicine packet.​

Click Analyze to start processing.​

Read the summary in the text box; you can edit, copy, or save it as .txt.​

If there is no recognizable text or the AI call fails, the app shows informative error messages and suggestions (e.g., improve image quality, check API key/network).​

Input and Output
Input formats: .jpg, .jpeg, .png medicine packet images.​

Recommended quality: clear image, minimal blur, text in focus, resolution around 720p or higher.​

Intermediate formats: optional .txt for OCR output and .log for debugging, if enabled.​

Output:

Shown in GUI via QTextEdit.
Can be saved as UTF‑8 .txt or captured via screenshot for reports.​

The summary typically includes purpose of the medicine, usage instructions, side effects, expiry or manufacturing details, storage instructions, and possible alternatives inferred by the model.

Advantages
User-friendly: Clean, minimal interface built with PyQt5, suitable for non-technical users.​

Time-saving: Automates reading and interpretation of complex medicine labels.​

Accessibility: Helps elderly users, visually challenged users, and those with low medical literacy.​

Scalable: Modular design makes it easier to plug in new OCR engines or AI models later.​

Secure handling: API keys managed via .env and local processing of images.​

Future Work
Potential enhancements for this repository:

Multilingual OCR and summaries for regional languages.​

Barcode/QR-code scanning to query structured drug databases.​

Text-to-speech for the generated summaries.​

Advanced analytics like interaction checks or dosage validation via external APIs.​

Contributors
Khune Pranav Vishwajit – B.Tech CSE (AIML)

Aditya Netaji Barmade – B.Tech CSE (AIML)