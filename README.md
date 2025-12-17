# 🛍 Outfit Color Suggestor Using Skin Tone Detection

A real-time styling assistant that uses a webcam to detect a user's skin tone and recommend the best clothing colors based on color theory. This project blends computer vision, machine learning, and fashion knowledge to help users choose outfit colors that enhance their appearance.

---
## 📸 Demo

![Demo Screenshot](./demo/Screenshot_2025-08-12_210320.png)

---

## 🚀 Features

- 📷 **Webcam Integration** – Capture live image from webcam  
- 🎨 **Skin Tone Detection** – Find dominant skin color using k-Means clustering  
- 👗 **Outfit Color Recommendations** – Suggest colors that match skin tone  
- 🔍 **Face Detection** – Ensure correct area is processed  
- 💡 **Fashion Theory Based Suggestions** – Uses complementary and harmonious colors

---

## 🧠 Technologies Used

| Technology   | Purpose                      |
|--------------|------------------------------|
| Python       | Main programming language    |
| OpenCV       | Image capture & processing   |
| scikit-learn | k-Means clustering algorithm |
| NumPy        | Numerical operations         |
| Flask/Tkinter| Web or desktop GUI           |
| Matplotlib   | Color visualization (optional) |

---

## ▶️ How to Use

1. Connect your webcam  
2. Run the application:  

```bash
python skin_tone_web.py
```

3. The application will open  
4. Capture your image → Process skin tone → View suggested outfit colors  

---

## 📂 Folder Structure

```
skin-tone-color-suggestor/
│
├── skin_tone_web.py               # Main application file
├── templates/                     # HTML templates (if using Flask)
│   ├── index.html
│   └── result.html
├── static/                        # CSS/JS files
├── requirements.txt               # Python dependencies
├── demo/                          # Demo screenshots
│   └── demo_image.png
└── README.md                      # Project documentation
```

---

## 🧪 Sample Code Snippet

```python
from sklearn.cluster import KMeans
import cv2

def extract_skin(image):
    # Convert image to HSV and apply skin color mask
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (0, 48, 80)
    upper = (20, 255, 255)
    skin_mask = cv2.inRange(hsv, lower, upper)
    return cv2.bitwise_and(image, image, mask=skin_mask)
```

---

## 👥 Team Members & Roles

- **Medabayina Poojitha** – Lead Developer & Skin Tone Analysis  
- **Annie Grace Ravi** – Fashion Theory & Outfit Recommendation Logic  
- **Sarayu Potnuru** – UI/UX Design & Project Documentation  

---

## 📌 Acknowledgments

- [OpenCV](https://opencv.org/)  
- [scikit-learn](https://scikit-learn.org/)  
- [Color Theory – Adobe](https://color.adobe.com)  

---

## 📄 License

This project is for academic purposes only. All rights reserved.
