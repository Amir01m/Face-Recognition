import os
import cv2
import face_recognition as fr
from load_faces import face_loader
from sql import can_log, insert_data
from tkinter import messagebox
# ---------- Camera ----------
def main():
    known_faces , known_names = face_loader()
    cap = cv2.VideoCapture(0)
    current_cam = 0
    cam_map = {ord('0'):0, ord('1'):1, ord('2'):2, ord('3'):3}
    
    new_cam = 0
    while True:
        try:
            ret, img = cap.read()
            if not ret:
                break
        except Exception as e:
            messagebox.showerror("Error",f"Error accessing camera {current_cam}: {e}")      
            break
        
        # Display current camera number
        
        cv2.putText(
        img,
        f"Camera {current_cam}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
        )
        
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        face_locations = fr.face_locations(rgb_img, model="hog")
        face_encodings = fr.face_encodings(rgb_img, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_faces, face_encoding, tolerance=0.5)
            name = "Unkown"

            if True in matches:
                index = matches.index(True)
                name = known_names[index]
                if can_log(name):
                    insert_data(name)
            
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

        cv2.imshow("Face Recognition for Quit press 'q'.", img)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        
        if key in cam_map:
            new_cam = cam_map[key]
            if new_cam != current_cam:
                cap.release()
                cap = cv2.VideoCapture(new_cam)
                if not cap.isOpened():
                    messagebox.showerror('Error',f"Camera {new_cam} is not available!")
                    cap = cv2.VideoCapture(current_cam)
                else:
                    current_cam = new_cam
                print(f"Switched to camera {new_cam}")



    cap.release()
    cv2.destroyAllWindows()

