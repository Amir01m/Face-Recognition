from tkinter import filedialog
import shutil
import os
import face_recognition as fr
import cv2
def add_pics():
    file = filedialog.askopenfilename(
        title="Selcet a file",
        filetypes=[("All Files","*.*"),("Images", "*.png;*.jpg")]
    )
    file_path = file
    file = cv2.imread(file)
    img = cv2.cvtColor(file,cv2.COLOR_BGR2RGB)
    face = fr.face_locations(file)

    dst = "./database"
    if len(face) > 0 and os.path.exists(dst):
        shutil.copy(file_path,dst)
    else: 
        os.mkdir(dst)
        shutil.copy(file_path,dst)
        
    return 
