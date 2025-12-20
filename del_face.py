import os
from tkinter import filedialog , messagebox

def del_face_file():
    files = filedialog.askopenfilenames(
        initialdir="./database",
        title="Select files",
        filetypes=[("All Files", "*.*"), ("Images", "*.png;*.jpg")]
    )
    print(files)
    try:
        confrim = messagebox.askyesno("Confirm Delete",
            f"Are you sure you want to delete {len(files)} file(s)?")    
        if confrim:
            for file in files:
                os.remove(file)
            messagebox.showinfo("Succes","all file have been deleted Succesfully")
        else:
            messagebox.showinfo("Nothing","you delete nothing...")
    except Exception as e:
        messagebox.showerror("Error",f"Error {e}")

