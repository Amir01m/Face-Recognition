import cv2
import os
from file_handl import take_pic_gui

def take_photos_with_camera():
    save_folder = "./database"    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return
            
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        cv2.imshow('Camera - Press s to take photo, q to quit', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            cap.release()
            cv2.destroyAllWindows()
            new_filename = take_pic_gui()

            filename = new_filename
            filename = str(filename)
            
            filepath = os.path.join(save_folder, filename)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            cv2.imwrite(filepath,frame)
            

        
        elif key == ord('q') or key == 27: 
            break
    
    cap.release()
    cv2.destroyAllWindows()
