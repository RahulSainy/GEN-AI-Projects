import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
import json
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('Google_API_KEY'))

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += str(page.extract_text())
    return text



# Set page configuration
st.set_page_config(
    page_title="Resume ATS Tracking",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)
sidebar = st.sidebar
sidebar.title('Navigation')
sidebar.markdown('Use this panel to navigate through the application and input your data.')
# Add a title and a subtitle
st.title('Resume ATS Tracking')
st.subheader('Upload your resume and paste the job description to get the ATS tracking response')

jd = st.text_area('Paste the Job Description')
uploaded_file = sidebar.file_uploader('Upload Resume', type=['pdf'])

submit = st.button('Submit')

# Process the uploaded file and job description when the submit button is clicked
if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        # input = input_prompt.format(text=text,jd=jd)
        response = get_gemini_response(input_prompt)
        response = response[1:-1]

        # Convert the response to a dictionary
        response_dict = json.loads(response)

        # Display the response in a structured way
        st.subheader('ATS Tracking Response:')
        st.markdown(f"**JD Match:** {response_dict['JD Match']}")
        st.markdown(f"**Missing Keywords:** {', '.join(response_dict['MissingKeywords'])}")
        st.markdown(f"**Profile Summary:** {response_dict['Profile Summary']}")