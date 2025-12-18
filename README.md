# Face Recognition CCTV System

A real-time face recognition system built with **Python**, **OpenCV**, and **face_recognition** that can detect and identify **multiple people simultaneously** using a webcam or CCTV camera.

This project is designed as a **practical, extendable AI/ML project**, suitable for learning, portfolio building, and future real-world applications.

---

## 🚀 Features

* 📷 Real-time face detection using camera feed
* 👥 Simultaneous recognition of multiple faces
* 🗂 Automatic loading of known faces from a folder
* 🏷 Identification by person name (based on image filename)
* ❓ Marks unknown faces as `Unknown`
* 🧠 Modular code structure (ready for expansion)

---

## 📁 Project Structure

```
project/
│
├── rec_face.py          # Main camera & recognition logic
├── load_faces.py        # Load face encodings from database folder
├── take_pic.py
├── filehandl.py
├── database/            # Face image database (user-defined)
│   ├── Amir.jpg
│   └── Ali.jpeg
└── README.md
```

---

## 🧠 How It Works

1. All face images are stored inside the `database/` folder.
2. Each image filename is treated as the **person's name**.
3. At startup, the program:

   * Reads all images using `glob`
   * Extracts face encodings
   * Stores them in memory
4. The camera feed is analyzed frame-by-frame:

   * Faces are detected
   * Each face is compared with known encodings
   * The best match name is displayed on screen

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install opencv-python face-recognition numpy tkinter shutil glob os datetime
```

> ⚠️ `face_recognition` requires **dlib**. Make sure it is installed correctly on your system.

### 2️⃣ Add Face Images

* Create a folder named `database`
* Add face images inside it
* Name each image after the person:

```
Amir.jpg
Sara.png
John.jpeg
```

### 3️⃣ Run the Program

```bash
python gui.py
```

Press **Q** to quit the camera.

---

## 🧪 Notes

* Each image should contain **only one clear face**
* Better lighting improves recognition accuracy
* The system currently uses the **HOG model** for faster performance

---

## 🔮 Future Improvements (Planned)

This project is **not finished** and is intentionally designed to be extended.

### Planned Features:

* 🖥 Graphical User Interface (GUI)✅
* ➕ Add new faces directly from the camera✅
* ❌ Remove faces from the system
* 🗄 User-managed face database
* 💾 Save face data using a database (SQLite)
* 🧠 Upgrade to Deep Learning models (CNN)
* 📊 Face detection logs and timestamps

Users will be able to **create their own database** using their own photos, and the system will recognize **only those individuals**.

---

## 🎯 Purpose

This project was built for:

* Learning face recognition concepts
* Understanding real-time computer vision systems
* Building a strong GitHub portfolio project
* Preparing for advanced Deep Learning implementations

---

## 📌 Author

Developed by **Amir**
Computer Engineering Student | Python & AI Enthusiast

---

⭐ If you like this project, feel free to star the repository!
