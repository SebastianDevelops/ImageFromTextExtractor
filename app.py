from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

def extract_text_from_image(image_path):
    try:
        # pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'
        # Open the image file
        img = Image.open(image_path)
        
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        # Get the image file from the request
        image_file = request.files['image']
        
        # Save the image to a temporary file
        temp_image_path = 'temp_image.png'
        image_file.save(temp_image_path)
        
        # Extract text from the image
        extracted_text = extract_text_from_image(temp_image_path)
        
        # Return the extracted text in the response
        response = {'text': extracted_text}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
