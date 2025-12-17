import cv2
import face_recognition as fr
import numpy as np
from load_faces import face_loader

# ---------- Camera ----------
def main():
    known_faces , known_names = face_loader()
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        face_locations = fr.face_locations(rgb_img, model="hog")
        face_encodings = fr.face_encodings(rgb_img, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_faces, face_encoding, tolerance=0.5)
            name = "Unkown"

            if True in matches:
                index = matches.index(True)
                name = known_names[index]

            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.putText(
                img,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_PLAIN,
                1.2,
                (0, 255, 0),
                2
            )

        cv2.imshow("Face Recognition", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

