from tkinter import filedialog, messagebox
import shutil
import os
import face_recognition as fr
import cv2
import tkinter as tk

def add_pics():
    add_win_tk_pic = tk.Toplevel()
    add_win_tk_pic.title("Name for Img")
    
    add_win_tk_pic.geometry("250x200")
    add_win_tk_pic.resizable(False, False)
    
    label = tk.Label(add_win_tk_pic, text="Enter the name")
    label.pack(side=tk.TOP, padx=20, pady=10)
    
    text_box = tk.Entry(add_win_tk_pic)
    text_box.pack(side=tk.TOP, padx=20, pady=10)

    def img_process():
        name = text_box.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        
        file = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All Files", "*.*"), ("Images", "*.png;*.jpg")]
        )
        
        if not file:
            messagebox.showwarning("Cancelled", "No file selected")
            return
        
        file_path = file
        
        try:
            file_img = cv2.imread(file_path)
            if file_img is None:
                messagebox.showerror("Error", "Could not read the image file")
                return
            
            img = cv2.cvtColor(file_img, cv2.COLOR_BGR2RGB)
            face = fr.face_locations(img)
            
            if len(face) == 0:
                messagebox.showerror("Error", "No face detected in the image")
                return

            dst_dir = "./database"
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            counter = 1
            dst_path = dst_dir
            while os.path.exists(dst_path):
                new_filename = f"{name}_{counter}.jpg"
                dst_path = os.path.join(dst_dir, new_filename)
                counter += 1            
            
            shutil.copy(file_path, dst_path)
            
            messagebox.showinfo("Success", f"Image saved as: {new_filename}")
            add_win_tk_pic.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return
    
    sbm_btn = tk.Button(add_win_tk_pic, text="Submit", command=img_process)
    sbm_btn.pack(padx=20, pady=10)
    
    cancel_btn = tk.Button(add_win_tk_pic, text="Cancel", command=add_win_tk_pic.destroy)
    cancel_btn.pack(padx=20, pady=10)

    return


#------------------gui--------------------
def take_pic_gui():
    add_win_tk_pic = tk.Toplevel()
    add_win_tk_pic.title("Name for Img")
    
    add_win_tk_pic.geometry("250x200")
    add_win_tk_pic.resizable(False, False)
    
    label = tk.Label(add_win_tk_pic, text="Enter the name")
    label.pack(side=tk.TOP, padx=20, pady=10)
    
    text_box = tk.Entry(add_win_tk_pic)
    text_box.pack(side=tk.TOP, padx=20, pady=10)
    result = {"filename" : None}
    def img_process():
        
        name = text_box.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        dst_dir = "./database"
        dst_path = dst_dir
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)

        counter = 1
        while os.path.exists(dst_path):
            new_filename = f"{name}_{counter}.jpg"
            dst_path = os.path.join(dst_dir, new_filename)
            counter += 1

        add_win_tk_pic.destroy()
        try:
            messagebox.showinfo("Success", f"Image saved as: {new_filename}")            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return
        result["filename"] = new_filename

    
    sbm_btn = tk.Button(add_win_tk_pic, text="Submit", command=img_process)
    sbm_btn.pack(padx=20, pady=10)
    
    cancel_btn = tk.Button(add_win_tk_pic, text="Cancel", command=add_win_tk_pic.destroy)
    cancel_btn.pack(padx=20, pady=10)
    
    text_box.focus_set()
    add_win_tk_pic.wait_window()

    return result["filename"]
