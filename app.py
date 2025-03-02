import streamlit as st
from fpdf import FPDF

def generate_resume(name, email, phone, education, experience, skills):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, name, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, email, ln=True, align='C')
    pdf.cell(200, 10, phone, ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, education)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, "Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, experience)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, skills)
    
    return pdf

st.title("📄 Resume & Portfolio Builder")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
education = st.text_area("Education")
experience = st.text_area("Work Experience")
skills = st.text_area("Skills")

if st.button("Generate Resume"):
    if name and email and phone and education and experience and skills:
        pdf = generate_resume(name, email, phone, education, experience, skills)
        pdf_output = "resume.pdf"
        pdf.output(pdf_output)
        with open(pdf_output, "rb") as file:
            st.download_button("📥 Download Resume", file, file_name="Resume.pdf", mime="application/pdf")
    else:
        st.warning("Please fill in all the fields!")
