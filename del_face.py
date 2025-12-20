import os
from tkinter import filedialog , messagebox
import tkinter as tk
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

def del_by_name():
    add_win_tk_pic = tk.Toplevel()
    add_win_tk_pic.title("Delete by name")
    
    add_win_tk_pic.geometry("250x200")
    add_win_tk_pic.resizable(False, False)
    
    label = tk.Label(add_win_tk_pic, text="Enter the name:")
    label.pack(side=tk.TOP, padx=20, pady=10)
    
    text_box = tk.Entry(add_win_tk_pic)
    text_box.pack(side=tk.TOP, padx=20, pady=10)
    
    def img_process():
        name = text_box.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        
        dst_dir = "./database"
                
        deleted_files = []
        try:
            for filename in os.listdir(dst_dir):
                if filename.startswith(name + "_") or filename.startswith(name):
                    file_path = os.path.join(dst_dir, filename)
                    os.remove(file_path)
                    deleted_files.append(filename)
            
            if deleted_files:
                messagebox.showinfo("Success", f"Deleted {len(deleted_files)} file(s):\n" + "\n".join(deleted_files))
            else:
                messagebox.showinfo("No files", f"No files found for name: {name}")
            
            add_win_tk_pic.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    sbm_btn = tk.Button(add_win_tk_pic, text="Submit", command=img_process)
    sbm_btn.pack(padx=20, pady=10)
    
    cancel_btn = tk.Button(add_win_tk_pic, text="Cancel", command=add_win_tk_pic.destroy)
    cancel_btn.pack(padx=20, pady=10)
    
    text_box.focus_set()
    add_win_tk_pic.wait_window()