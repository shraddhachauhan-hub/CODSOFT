import cv2
import os
import pandas as pd
from datetime import datetime

# ---------------------------
# Load Trained Model
# ---------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/trainer.yml")

# ---------------------------
# Load Face Detector
# ---------------------------
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ---------------------------
# Load Names from Dataset
# ---------------------------
names = {}

for idx, person in enumerate(os.listdir("dataset")):
    person_path = os.path.join("dataset", person)

    if os.path.isdir(person_path):
        names[idx] = person

# ---------------------------
# Create Attendance Folder
# ---------------------------
if not os.path.exists("attendance"):
    os.makedirs("attendance")

attendance_file = "attendance/attendance.csv"

# Store already marked names
marked_names = set()

# ---------------------------
# Start Webcam
# ---------------------------
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Could not access webcam.")
    exit()

print("FaceGuard AI Started")
print("Press ESC to Exit")

while True:

    ret, img = cam.read()

    if not ret:
        print("Failed to capture frame.")
        break

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Face Counter
    cv2.putText(
        img,
        f"Faces: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    for (x, y, w, h) in faces:

        face_roi = gray[y:y+h, x:x+w]

        id, confidence = recognizer.predict(
            face_roi
        )

        # Lower confidence value = better match
        if confidence < 70:

            name = names.get(id, "Unknown")

            confidence_percent = max(
                0,
                min(
                    100,
                    round(100 - confidence)
                )
            )

            # Name + Confidence
            cv2.putText(
                img,
                f"{name} ({confidence_percent}%)",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            # Mark Attendance Once
            if name not in marked_names:

                marked_names.add(name)

                now = datetime.now()

                attendance_data = pd.DataFrame({
                    "Name": [name],
                    "Date": [
                        now.strftime("%Y-%m-%d")
                    ],
                    "Time": [
                        now.strftime("%H:%M:%S")
                    ]
                })

                if os.path.exists(attendance_file):

                    attendance_data.to_csv(
                        attendance_file,
                        mode='a',
                        header=False,
                        index=False
                    )

                else:

                    attendance_data.to_csv(
                        attendance_file,
                        index=False
                    )

                print(
                    f"Attendance Marked: {name}"
                )

            rectangle_color = (0, 255, 0)

        else:

            cv2.putText(
                img,
                "Unknown",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            rectangle_color = (0, 0, 255)

        # Draw Rectangle
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            rectangle_color,
            2
        )

    cv2.imshow(
        "FaceGuard AI",
        img
    )

    key = cv2.waitKey(1)

    # ESC Key
    if key == 27:
        break

# ---------------------------
# Cleanup
# ---------------------------
cam.release()
cv2.destroyAllWindows()