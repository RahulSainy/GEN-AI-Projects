# Simple Resume ATS Tracking

## Project Flow

![Project Flow](ATS%20Resume%20Tracker%20Project%20flow%20TLDR.png)
1. **PDF Text:** The application starts by extracting text from a PDF file. This is done using the PyPDF2 library.

2. **API Response:** The extracted text is then sent to the Gemini API. The API processes the text and returns a response.

3. **PyPDF2 to Text:** The PyPDF2 library converts the PDF file into text. This text is then processed further.

4. **Gemini Using:** The processed text is sent to the Gemini API for further analysis.

## Technologies Used

- **Streamlit:** Streamlit is used for creating the web application. It provides an easy way to create beautiful, interactive web applications.

- **PyPDF2:** PyPDF2 is used for extracting text from PDF files. It provides a simple and efficient way to handle PDF files in Python.

- **Gemini:** Gemini is used for processing the text extracted from the PDF files. It provides powerful text analysis capabilities.

## Getting Started

To start this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/RahulSainy/GEN-AI-Projects.git
cd Simple Resume ATS Tracking
pip install -r requirements.txt
streamlit run app.py
