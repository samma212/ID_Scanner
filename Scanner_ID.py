import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np


st.title("ID Scanner App")

uploaded_image = st.file_uploader("Please upload an image...", type=["jpg", "png", "jpeg",'webp'])

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def Extrat_text_fun(img):
    text = pytesseract.image_to_string(img)
    return text



if uploaded_image is not None:
    img = Image.open(uploaded_image)
    # convert image --> array
    img_array = np.array(img)
    #show img on st
    st.image(img_array, caption="Uploaded Image...")
    
    with st.spinner('Extracting text from your ID...'):
        ext_text = Extrat_text_fun(img_array)
        st.header("Extracted Text:")
        text_list = ext_text.splitlines()
        st.write(text_list)



