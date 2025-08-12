# step3_cluster_skin_color.py

import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_skin_color(image_path, k=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize for faster processing
    image = cv2.resize(image, (200, 200))

    # Optional: Crop central region (assumed to be skin)
    h, w, _ = image.shape
    crop = image[h//4:h*3//4, w//4:w*3//4]

    # Flatten image to (num_pixels, 3)
    pixels = crop.reshape((-1, 3))

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # Get dominant color (most frequent cluster)
    unique, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant = kmeans.cluster_centers_[unique[np.argmax(counts)]]

    dominant_color = tuple(map(int, dominant))
    print("Dominant Skin Color (RGB):", dominant_color)

    # Show the color
    swatch = np.zeros((100, 300, 3), dtype=np.uint8)
    swatch[:, :] = dominant_color

    plt.imshow(swatch)
    plt.title(f"Dominant Skin Color: RGB {dominant_color}")
    plt.axis('off')
    plt.show()

    return dominant_color

if __name__ == "__main__":
    extract_skin_color("face_capture.jpg")
