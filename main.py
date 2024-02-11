from flask import Flask, render_template, request
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

@app.route('/upload1', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input1 = request.form['procedure']
        input2 = request.form['state']
        input3 = request.form['cost']
        if "$" in input3:
            input3 = input3[1:]
        result = process_input(input1, input2, input3)  # Adjusted to handle three inputs
        return render_template('index.html', variable=result)
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

        state = ''
        cost = ''
        procedure = ''
        for text in texts:
            if text in ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
                        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
                        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
                        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']:
                state = text
                break
            elif text in ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", 
                          "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", 
                          "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", 
                          "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", 
                          "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", 
                          "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", 
                          "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", 
                          "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", 
                          "Washington", "Wisconsin", "West Virginia", "Wyoming"]:
                state = text
                break
        cost = 0
        costMax = 0
        price = 0
        count = 0
        for text in texts:
            price = 0
            if (text[0]=="S" and text[1].isdigit()) or text[0]=="$":
                count+=1
                price = int(text[1:])
                cost+= price
                if price> costMax:
                    costMax = price
        if count != 1:
            cost = cost-costMax
        
        entriesRecieved = entries.entriesList
        print(texts)

        
        found = False
        
        for i in entriesRecieved:
            if not found:
                if texts[0] in i:
                    procedure = texts[0]
                    found = True
                    break
            else:
                break
                
                
        texts = [procedure, state, cost]
        # Render the homepage with extracted texts
        print(texts)
        result = process_input(texts[0], texts[1], texts[2])
        texts = [result]
        return render_template('index.html', extracted_texts=texts)
    return 'No file uploaded', 400



if __name__ == '__main__':
    app.run(debug=True)
