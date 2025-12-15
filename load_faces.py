import cv2
import face_recognition as fr
import numpy as np
import glob
import os

# ---------- Load known faces from folder ----------
def face_loader(known_faces = [],known_names = []):

    image_paths = glob.glob("database/*")

    for img_path in image_paths:
        name = os.path.splitext(os.path.basename(img_path))[0]
        img = fr.load_image_file(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodings = fr.face_encodings(img)

        if len(encodings) > 0:
            known_faces.append(encodings[0])
            known_names.append(name)
        else:
            print(f"⚠️ No face found in {img_path}")
    return known_faces , known_names
