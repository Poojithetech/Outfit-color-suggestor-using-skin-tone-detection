from flask import Flask, render_template, request
import cv2
import numpy as np
from collections import Counter
import os
import base64
import re

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_dominant_skin_color(image):
    image = cv2.resize(image, (100, 100))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([50, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)
    pixels = result.reshape(-1, 3)
    pixels = [tuple(pixel) for pixel in pixels if not all(v == 0 for v in pixel)]

    if not pixels:
        return (128, 128, 128)

    most_common = Counter(pixels).most_common(1)[0][0]
    return tuple(int(c) for c in most_common)

def get_recommended_colors(rgb):
    r, g, b = rgb
    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    def linkify(color_name):
        query = re.sub(r"\s+", "+", color_name + " outfit")
        return {
            "amazon": f"https://www.amazon.in/s?k={query}",
            "flipkart": f"https://www.flipkart.com/search?q={query}"
        }

    if luminance < 100:
        colors = [("🤍", "Ivory"), ("💙", "Sky Blue"), ("💜", "Lilac"), ("💚", "Mint"), ("🩵", "Powder Blue")]
    elif luminance < 170:
        colors = [("🧡", "Coral"), ("🫒", "Olive Green"), ("🟧", "Rust Orange"), ("💜", "Purple"), ("🌊", "Teal")]
    else:
        colors = [("🟥", "Maroon"), ("💚", "Forest Green"), ("🧵", "Burgundy"), ("🟤", "Brown"), ("🖤", "Black")]

    return [{
        "emoji": emoji,
        "name": name,
        "links": linkify(name)
    } for emoji, name in colors]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    image_data = request.form['image_data'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    image_path = os.path.join(UPLOAD_FOLDER, 'captured.jpg')

    with open(image_path, 'wb') as f:
        f.write(image_bytes)

    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    dominant_color = get_dominant_skin_color(image)
    suggestions = get_recommended_colors(dominant_color)
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')

    return render_template('result.html',
                           image_data=encoded_image,
                           color=dominant_color,
                           suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
