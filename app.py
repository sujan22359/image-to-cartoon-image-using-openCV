from flask import Flask, render_template, request, redirect, url_for
from cartoonify import cartoonify_image
import io
import base64
from PIL import Image
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cartoonify', methods=['POST'])
def cartoonify():
    if 'image' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))    
    image = Image.open(file)   
    cartoon = cartoonify_image(image)    
    _, buffer = cv2.imencode('.jpg', cartoon)
    cartoon_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return render_template('cartoonify.html', cartoon_base64=cartoon_base64)

if __name__ == '__main__':
    app.run(debug=True)
