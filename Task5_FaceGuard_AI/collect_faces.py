import cv2
import os

name = input("Enter Name: ")

path = f"dataset/{name}"

if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

count = 0

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(
            img,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )

        count += 1

        cv2.imwrite(
            f"{path}/{count}.jpg",
            gray[y:y+h,x:x+w]
        )

        cv2.imshow('Collecting Faces', img)

    k = cv2.waitKey(100) & 0xff

    if k == 27:
        break

    elif count >= 50:
        break

cam.release()
cv2.destroyAllWindows()

print("Dataset Collected Successfully")