🌌 Star Constellations Game  
A Hand-Tracking Interactive Constellation Creator using MediaPipe + OpenCV*

✨ Overview  
**Star Constellations Game** is an interactive computer-vision project where users trace stars using their **index finger** in front of the webcam.

🔴 Random red dots appear at the start  
🟢 When the user hovers their finger → dots turn green  
🌟 Selecting a dot unlocks the next set of nearby stars  
✨ After completing multiple steps → a final constellation is formed  
📘 The app displays information about the constellation

This project uses **MediaPipe Hand Tracking**, **OpenCV**, and Python logic for selection paths.


 🎥 Demo  



📁 Project Structure

ConstellationsGame/
│── assets/ # Images, demo videos, UI elements
---
│── constellations.py # Contains constellation definitions / logic
---
│── utils.py # Helper functions (distance, drawing, etc.)
---
│── main.py # Application entry point (hand-tracking + logic)
---
│── requirements.txt # Python dependencies
---
│── README.md



🛠️ Tech Used
- **Python 3.10**
- **MediaPipe 0.10.9**
- **OpenCV**
- **NumPy**

---

# 🚀 How to Run the Project

## 1️⃣ Install Python 3.10 (Required)
MediaPipe only supports Python **3.7–3.10**.

Download Python 3.10.11 here:  
https://www.python.org/downloads/release/python-31011/

Check installation:
py -3.10 --version


## 2️⃣ Clone this Repository

git clone https://github.com/HarshitaGupta-610/ConstellationsGame.git
cd ConstellationsGame



## 3️⃣ Create Virtual Environment (VERY IMPORTANT)

py -3.10 -m venv .venv

Activate it:

### Windows:
..venv\Scripts\activate



### Mac/Linux:
source .venv/bin/activate


## 4️⃣ Install Requirements

pip install -r requirements.txt



If MediaPipe fails, manually install:

pip install mediapipe==0.10.9 opencv-python numpy



## 5️⃣ Run the App

python main.py


Your webcam will open, and the red stars will appear.

---

# 🎮 How to Play  

1. Move your **index finger** near a red dot  
2. It will turn **green**  
3. This unlocks the next neighborhood of stars  
4. Repeat for 4–5 steps  
5. A complete constellation is drawn  
6. Information about it appears on screen  

---

# ⭐ Features  
✔ Real-time hand tracking  
✔ Dynamic star-selection logic  
✔ Multi-step constellation creation  
✔ Fully interactive webcam UI  
✔ Customizable constellation paths  

---

# 🧩 Future Enhancements  
- Add more constellation sets  
- Add animations / star glow effect  
- Save final constellation as PNG  
- Add menu screen and difficulty modes  

---

