# step5_display_results.py

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors  # ✅ Correct import
from step3_cluster_skin_color import extract_skin_color
from step4_recommend_colors import recommend_outfit_colors

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def show_results(image_path):
    skin_rgb = extract_skin_color(image_path)
    recommendations = recommend_outfit_colors(skin_rgb)

    # Load and convert the original image
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create swatch for dominant color
    swatch = np.zeros((100, 300, 3), dtype=np.uint8)
    swatch[:, :] = skin_rgb

    # Prepare outfit color swatches
    color_patches = np.zeros((len(recommendations) * 50, 300, 3), dtype=np.uint8)
    for i, color in enumerate(recommendations):
        hex_color = color.lower().replace(" ", "")
        try:
            rgb_val = tuple(int(255 * x) for x in colors.to_rgb(hex_color))
        except:
            rgb_val = (200, 200, 200)  # fallback gray
        color_patches[i * 50:(i + 1) * 50, :] = rgb_val

    # Create a figure
    plt.figure(figsize=(12, 6))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Captured Image")
    plt.axis('off')

    # Skin tone swatch
    plt.subplot(1, 3, 2)
    plt.imshow(swatch)
    plt.title(f"Skin Tone: {skin_rgb}")
    plt.axis('off')

    # Recommended colors
    plt.subplot(1, 3, 3)
    plt.imshow(color_patches)
    plt.title("Recommended Outfit Colors")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_results("face_capture.jpg")
