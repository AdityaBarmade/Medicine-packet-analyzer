# Medicine Packet Analyzer

Medicine Packet Analyzer is a Python-based desktop application that reads text from medicine packet images and converts it into clear, structured medical information using OCR and an AI model (Google Gemini).

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [System Architecture](#system-architecture)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Input and Output](#input-and-output)  
- [Advantages](#advantages)  
- [Future Work](#future-work)  
- [Contributors](#contributors)  
- [License](#license)  

## Overview

Medicine packets usually contain critical details such as drug name, dosage, expiry, warnings, and usage instructions, which are often hard to read or understand for non-experts.[file:21] This project lets users upload an image of a medicine strip or box, extracts text via OCR, and then uses Gemini to generate a patient-friendly explanation of the medicine information.

## Features

- Modern PyQt5 GUI to upload medicine images and view results.  
- Image preprocessing (resize, grayscale, enhancement) before OCR for better recognition. 
- Dual OCR pipeline using EasyOCR (primary) and Tesseract (fallback) to improve accuracy.
- AI-powered summarization with Google Gemini API: usage, warnings, dosage, expiry, alternatives, and more. 
- Scrollable, editable result box with copy-to-clipboard and save-to-file options.
- Basic error handling when no text is detected or the AI service fails.

## System Architecture

The project follows a layered architecture to keep components modular and maintainable.

- **User Interface Layer (PyQt5):** GUI for selecting images, starting analysis, and visualizing results. 
- **Image Processing Layer (OpenCV & PIL):** Cleans and prepares images for OCR.
- **OCR Engine Layer (EasyOCR / Tesseract):** Extracts raw text from the processed image. 
- **AI Analysis Layer (Gemini API):** Interprets OCR text using an LLM to produce structured summaries.
- **Output Rendering Layer (PyQt5):** Displays processed information and supports user actions like copy/save.

## Tech Stack

| Component          | Technology / Tool                        |
|--------------------|-------------------------------------------|
| Programming        | Python 3.10+                             |
| GUI Framework      | PyQt5                                    |
| OCR Engines        | EasyOCR, Tesseract OCR                   |
| Image Processing   | OpenCV, Pillow (PIL)                     |
| AI / LLM           | Google Gemini API                        |
| Config Management  | `python-dotenv` with `.env` file         |
| Environment / IDE  | Local Python environment                 |

These tools were selected for robust OCR, flexible GUI design, and easy integration with AI services.

## Project Structure 
Medicine-packet-analyzer/

    ├── main.py # CLI entry point
    ├── ui_tkinter.py # GUI application
    ├── analyzer.py # OCR + AI orchestration
    ├── ocr_engine.py # OCR processing
    ├── gemini_ai.py # Gemini API integration
    ├── requirements.txt # Python dependencies
    ├── README.md # Project documentation
    │
    └── assets/ # Screenshots
       ├── ui.png # Main application UI
       ├── upload.png # Image upload screen
       └── output.png # Sample AI output


## Installation

1. **Clone the repository**
   git clone https://github.com/AdityaBarmade/Medicine-packet-analyzer.git
   
### Step 2: Environment Setup

**Virtual Environment (Recommended)**
Create virtual environment
python -m venv medicine_env

Activate (Windows)
medicine_env\Scripts\activate

Activate (Linux/macOS)
source medicine_env/bin/activate
 
3. **Install dependencies**

pip install -r requirements.txt

### Step 4: Tesseract OCR Setup

**Windows:**
1. Download Tesseract from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install and add to PATH

**Linux:**
sudo apt update
sudo apt install tesseract-ocr

**macOS:**
brew install tesseract

2. Edit `.env` file:

**Get FREE Gemini API key:** [Google AI Studio](https://makersuite.google.com/app/apikey)

4. **Configure the Gemini API key**

Create a `.env` file in the project root:
GEMINI_API_KEY=your_gemini_api_key_here

The key is loaded using `python-dotenv` so you do not need to hardcode it in `gemini_ai.py`.

## Usage

### CLI Mode

Run analysis from the terminal with an image path:


This prints the AI-generated analysis in the console.

### GUI Mode

Launch the desktop GUI:


Then:

1. Click **Browse Image** and choose a `.jpg`, `.jpeg`, or `.png` file of a medicine packet. 
2. Click **Analyze** to start processing.[file:21]  
3. Read the summary in the text box; you can edit, copy, or save it as `.txt`.

If there is no recognizable text or the AI call fails, the app shows informative error messages and suggestions (e.g., improve image quality, check API key/network).

## Input and Output

- **Input formats:** `.jpg`, `.jpeg`, `.png` medicine packet images.
- **Recommended quality:** clear image, minimal blur, text in focus, resolution around 720p or higher.  
- **Intermediate formats:** optional `.txt` for OCR output and `.log` for debugging, if enabled.
- **Output:**  
  - Shown in GUI via `QTextEdit`.  
  - Can be saved as UTF‑8 `.txt` or captured via screenshot for reports.
  
## Sample Output:

Medicine Name: Paracetamol 500mg

Purpose: Pain relief, fever reduction

Dosage: 1-2 tablets every 6-8 hours

Warnings: Avoid alcohol, consult doctor if pregnant

Expiry: Check packaging

The summary typically includes purpose of the medicine, usage instructions, side effects, expiry or manufacturing details, storage instructions, and possible alternatives inferred by the model.

## Advantages

- **User-friendly:** Clean, minimal interface built with PyQt5, suitable for non-technical users. 
- **Time-saving:** Automates reading and interpretation of complex medicine labels. 
- **Accessibility:** Helps elderly users, visually challenged users, and those with low medical literacy. 
- **Scalable:** Modular design makes it easier to plug in new OCR engines or AI models later.  
- **Secure handling:** API keys managed via `.env` and local processing of images.  


## Troubleshooting

| Issue | Solution |
|-------|----------|
| `No module named 'PyQt5'` | `pip install -r requirements.txt` |
| `Tesseract not found` | Install Tesseract and add to PATH |
| `Gemini API error` | Check `.env` file and internet connection |
| `No text detected` | Use clearer image, better lighting |
| `pip install easyocr fails` | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu` |

## Advantages

- 🎯 **Accessible** - Helps elderly/low-vision users
- ⚡ **Fast** - OCR + AI in seconds
- 🔒 **Secure** - Local processing, secure API keys
- 📱 **Cross-platform** - Windows/Linux/macOS
- 🛠️ **Modular** - Easy to extend/modify

## Future Work

- 🌐 Multilingual OCR support
- 📱 Mobile app version
- 🔊 Text-to-speech output
- 🩺 Drug interaction checker
- 📊 Batch processing mode

## Contributors

| Name | Roll No | Contribution |
|------|---------|--------------|
| Khune Pranav Vishwajit | 16 | Core development, GUI |
| Aditya Netaji Barmade | 33 | OCR integration, AI |


## License

MIT License © 2025 Medicine Packet Analyzer

---

*⭐ Star this repo if it helps! Questions? Open an [Issue](https://github.com/AdityaBarmade/Medicine-packet-analyzer/issues/new)

## License

MIT License - feel free to use and modify.



   





