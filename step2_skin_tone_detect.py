# step2_skin_tone_detect.py

import cv2

def capture_face_from_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam.")
        return

    print("Press 's' to save the image and exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Webcam - Face Capture", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            # Save frame to file
            cv2.imwrite("face_capture.jpg", frame)
            print("Image saved as face_capture.jpg")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_face_from_webcam()
