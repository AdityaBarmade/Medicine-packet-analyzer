import requests
import json
import os

GEMINI_API_KEY = "<API-KEY>"  # Add your Gemini API Key here
GEMINI_MODEL_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def analyze_medicine_details(extracted_text: str) -> str:
    prompt = f"""
You are an intelligent assistant for analyzing text extracted from medicine packets. Your goal is to extract and summarize the following details:

- **Why Medicine is Used for**  
- **Medicine Name**  
- **Manufacturer**  
- **Expiry Date**  
- **Usage Instructions**  
- **Dosage**  
- **Side Effects or Warnings**  
- **Advantages and Benefits**  
- **Storage Instructions**  
- **Any license numbers or trademarks**  

IMPORTANT:
- Highlight **important points** like **Medicine Name**, **Usage Instructions**, **Side Effects**, **Advantages**, etc., clearly.
- If **any information** such as expiry date, side effects, or advantages is **missing or unclear**, use your knowledge to infer the most common info for that medicine.
- Ensure the **information is accurate, concise, and medically helpful**. 
- **Suggest how to use the medicine if a doctor is not available**, based on the provided details.
- **Do not leave any section blank**. If necessary, research and provide inferred or common details.
- Always respond in a **positive and helpful tone**.
- Provide the **information in plain, readable format** without markdown or special formatting.

Text from packet:
\"\"\"{extracted_text}\"\"\"

Now return all extracted and inferred information with clear highlights and suggestions on usage, grouped clearly, and formatted in a helpful tone.
    """

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(GEMINI_MODEL_URL, headers=headers, json=data)
        result = response.json()
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: Could not get a valid response from Gemini."
    except Exception as e:
        return f"Error analyzing with Gemini: {str(e)}"
