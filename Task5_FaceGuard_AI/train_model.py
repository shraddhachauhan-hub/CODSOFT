import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataset'

faces = []
ids = []

label_dict = {}
current_id = 0

for person in os.listdir(path):

    label_dict[current_id] = person

    person_path = os.path.join(path, person)

    for image in os.listdir(person_path):

        img_path = os.path.join(
            person_path,
            image
        )

        pil_img = Image.open(
            img_path
        ).convert('L')

        img_numpy = np.array(
            pil_img,
            'uint8'
        )

        faces.append(img_numpy)
        ids.append(current_id)

    current_id += 1

recognizer.train(
    faces,
    np.array(ids)
)

if not os.path.exists("models"):
    os.makedirs("models")

recognizer.write(
    "models/trainer.yml"
)

print("Training Complete")