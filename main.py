from flask import Flask, render_template, request
import torch
import torch.backends
import cv2
import easyocr
import numpy as np
import pandas as pd
from my_script import process_input
import entries


app = Flask(__name__)
reader = easyocr.Reader(['en'])

@app.route('/', methods=['GET'])
def index():
    # Render the upload form
    return render_template('index.html')

@app.route('/', methods=['GET'])
def index1():
    # Render the upload form
    return render_template('index.html')

@app.route('/scan_image')
def scan_image():
    return render_template('scan_image.html')

@app.route('/interpret')
def interpret():
    return render_template('interpret.html')

@app.route('/data')
def show_text_file_content():
    # Open and read the content of your .txt file
    file_path = r"templates\viewData.txt"  # Adjust the path as necessary
    with open(r"templates\viewData.txt", 'r') as file:
        file_content = file.read()
    
    # Pass the content to your HTML template
    return render_template('data.html', text_content=file_content)

@app.route('/upload1', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input1 = request.form['procedure']
        input2 = request.form['state']
        input3 = request.form['cost']
        if "$" in input3:
            input3 = input3[1:]
        if len(input2)>2:
            input2 = entries.state_abbreviations[input2]
        result = process_input(str(input1), str(input2), str(input3))
        texts = [result]
        return render_template('home.html', extracted_texts=texts)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # Read the uploaded image file
        image_stream = uploaded_file.stream.read()
        numpy_image = np.frombuffer(image_stream, np.uint8)
        img = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR)
        
        # Use EasyOCR to extract text
        results = reader.readtext(img)
        texts = [text[1] for text in results]
        print(texts)
        state = ''
        cost = ''
        procedure = ''
        
        # Mapping of state full names to their abbreviations
        for text in texts:
            # Check if text is already an abbreviation
            if text in entries.state_abbreviations.values():
                state = text
            # Check if text is a full name and map it to its abbreviation
            elif text in entries.state_abbreviations:
                state = entries.state_abbreviations[text]

        cost = 0
        costMax = 0
        price = 0
        count = 0

        for text in texts:
            price = 0
            if text[0] == "S" and text[1].isdigit() or (text[0] == "$") or (all(char.isdigit() for char in text)):
                count+=1
                price = int(text[1:])
                cost+= price
                if price> costMax:
                    costMax = price

        if count != 1:
            cost = cost-costMax
        
        entriesRecieved = entries.entriesList
        
        found = False
        
        for i in entriesRecieved:
            if not found:
                for text in texts:
                    if not found:
                        if text.lower() in i.lower():
                            procedure = text
                            found = True
                            break
            else:
                break
                                
        texts = [procedure, state, cost]
        # Render the homepage with extracted texts
        print(texts[0], texts[1], texts[2])
        texts[2] = str(texts[2])
     
        result = process_input(str(texts[0]), str(texts[1]), str(texts[2]))
        texts = [result]
        
        return render_template('home.html', extracted_texts=texts)
    return 'No file uploaded', 400


if __name__ == '__main__':
    app.run(debug=True)