# ID Scanner App

The ID Scanner App is a Streamlit-based web application that allows users to upload an image of an ID and extract text from it using Optical Character Recognition (OCR) with Tesseract.

## Features

- Upload images in JPG, PNG, JPEG, or WEBP formats.
- Display the uploaded image.
- Extract and display text from the uploaded image using Tesseract OCR.

## Requirements

- Python 3.6 or higher
- Streamlit
- OpenCV
- pytesseract
- Pillow
- numpy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ID_Scanner_App.git
    cd ID_Scanner_App
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

4. Update the `tesseract_cmd` path in the `Scanner_ID.py` file to the location where Tesseract is installed on your system:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run Scanner_ID.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image of an ID and wait for the text to be extracted and displayed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.