import os
from gui import gui
save_folder = "./database"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

if __name__ == "__main__":
    gui()