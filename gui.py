import tkinter as tk
from rec_face import main
from file_handl import add_pics
from take_pic import take_photos_with_camera
#-------------------GUI--------------------
def gui():
    root = tk.Tk()
    root.title("Face Recognition System")
    root.geometry("400x400")
    root.resizable(False, False)
    def add_but_win():
        add_win = tk.Toplevel(root)
        add_win.title("Add IMG")
        add_win.geometry("250x250")
        add_win.resizable(False,False)

        del_but = tk.Button(add_win, text="Select Pic", font=("Arial", 10), width=12, height=2,command=add_pics)
        del_but.pack(side=tk.TOP, padx=20,pady=20)

        take_pic = tk.Button(add_win,text="Take a Picture",font=("Arial", 10), width=12, height=2,command=take_photos_with_camera)
        take_pic.pack(padx=20,pady=20)
        
        exit_btn = tk.Button(add_win, text="Exit", font=("Arial", 9), width=12, height=2,command=add_win.destroy,fg="white",bg="red")
        exit_btn.pack(side=tk.BOTTOM, padx=20,pady=20)
        
      

    

    tk.Label(root, text="Face Recognition", font=("Arial", 16, "bold"), fg="green").pack(pady=30)
    
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, pady=50)
    
    del_but = tk.Button(bottom_frame, text="Delete Picture", font=("Arial", 10), width=12, height=2)
    del_but.pack(side=tk.LEFT, padx=20)
    
    add_but = tk.Button(bottom_frame, text="Add Picture", font=("Arial", 10), width=12, height=2,command=add_but_win)
    add_but.pack(side=tk.RIGHT, padx=20)
    
    camera_btn = tk.Button(root, text="Start Camera", font=("Arial", 12, "bold"), 
                          bg="blue", fg="white", width=15, height=2,command=main)
    camera_btn.pack(side=tk.BOTTOM, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    gui()