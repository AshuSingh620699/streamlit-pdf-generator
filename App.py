import streamlit as st  # Used for creating the web app UI.
from reportlab.lib.pagesizes import letter      # Defines the page size of the PDF (Letter size: 8.5 x 11 inches).
from reportlab.pdfgen import canvas     # The canvas module is used to create and manipulate PDF files.
import io       # Provides BytesIO, which helps handle file-like objects in memory instead of writing them to disk.

def generate_pdf(text):
    buffer = io.BytesIO()   # A BytesIO object is used to store the generated PDF in memory.

    c = canvas.Canvas(buffer, pagesize=letter)      # initializes the PDF document.
    c.drawString(100, 750, text)    # writes the user's text onto the PDF at position (100, 750).
    c.save()
    buffer.seek(0)      # resets the buffer’s position for reading.
    return buffer       # Finally, it returns the in-memory PDF file.

st.title("PDF Generator App")       # Sets the title of the web app.
user_input = st.text_area("Enter Text for PDF")     # Creates a text area where the user can type input.

if st.button("Generate PDF"):   # When clicked, it calls generate_pdf(user_input).
# The generated PDF is stored in pdf_buffer.

    pdf_buffer = generate_pdf(user_input)

    # allows users to download the PDF with
    # label: "Download PDF"
    # data: pdf_buffer (the generated file)
    # file_name: "generated.pdf"
    # mime type: "application/pdf" (indicating it’s a PDF file)
    st.download_button(label="Download PDF", data=pdf_buffer, file_name="generated.pdf", mime="application/pdf")


# To run the app : python -m streamlit run app.py