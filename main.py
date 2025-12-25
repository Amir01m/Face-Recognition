import os
from gui import gui
from sql import create_table
save_folder = "./database"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

create_table()
    
if __name__ == "__main__":
    gui()