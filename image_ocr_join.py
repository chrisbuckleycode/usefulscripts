import pytesseract
from PIL import Image
import glob
import datetime

# sudo apt install tesseract-ocr
# Remember venv FIRST then:
# python3 -m pip install pytesseract
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Function to perform OCR on a single image
def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Get all the png files in the current directory
png_files = glob.glob("*.png")

# Perform OCR on each png and store the extracted text
extracted_texts = []
for file in png_files:
    # Using PIL to open the image
    img = Image.open(file)
    extracted_text = ocr_image(file)
    extracted_texts.append(extracted_text)

# Generate the timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Save the extracted texts to a single file
output_file = f"kb-{timestamp}.txt"
with open(output_file, 'w') as file:
    file.write('---------------------------------\n'.join(extracted_texts))

print(f"Extracted texts saved to {output_file}")
