import cv2
import mediapipe as mp
import numpy as np
import random
import math
import streamlit as st

# ---------------- Streamlit Setup ----------------
st.set_page_config(page_title="Constellation Builder", layout="wide")
st.title("🌌 Hand Gesture Constellation Builder")

st.write("Move your hand in front of webcam to connect stars and form constellations!")

# Button to start webcam
run = st.checkbox("Start Webcam")

# ---------------- Mediapipe Init ----------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Window size
WIDTH, HEIGHT = 1280, 720

# Function to calculate distance
def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Generate random star points without overlap
num_stars = 50
stars = []
MIN_DISTANCE = 70
while len(stars) < num_stars:
    candidate = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
    if all(distance(candidate, s) > MIN_DISTANCE for s in stars):
        stars.append(candidate)

selected_stars = []
connections = []

# Selection thresholds
SELECTION_RADIUS = 60
NEIGHBOR_RADIUS = 250

# Constellation templates
constellations = {
    "Orion": {"size": 7, "info": "Orion is one of the brightest constellations, known as the Hunter.\nIt contains the famous Orion’s Belt."},
    "Big Dipper": {"size": 7, "info": "The Big Dipper is part of Ursa Major.\nIt has been used for navigation for centuries."},
    "Cassiopeia": {"size": 5, "info": "Cassiopeia looks like a 'W' in the sky.\nIt is named after the vain queen in Greek mythology."},
    "Cygnus": {"size": 6, "info": "Cygnus is also called the Northern Cross.\nIt represents a swan flying across the Milky Way."},
    "Scorpius": {"size": 8, "info": "Scorpius resembles a scorpion.\nIt contains Antares, a bright red star."},
    "Leo": {"size": 9, "info": "Leo represents a lion in the sky.\nIt contains the bright star Regulus."},
    "Taurus": {"size": 7, "info": "Taurus is the bull constellation.\nIt contains the Pleiades star cluster."},
    "Gemini": {"size": 8, "info": "Gemini represents the twin brothers Castor and Pollux.\nBoth stars are bright and close together."},
    "Aquarius": {"size": 10, "info": "Aquarius is the water bearer.\nIt is one of the oldest constellations in the zodiac."},
    "Pegasus": {"size": 9, "info": "Pegasus is named after the winged horse.\nIt contains the Great Square of Pegasus."},
    "Andromeda": {"size": 7, "info": "Andromeda contains the Andromeda Galaxy.\nIt is the closest spiral galaxy to the Milky Way."},
    "Sagittarius": {"size": 8, "info": "Sagittarius is the archer.\nIt points toward the center of our galaxy."}
}

# ---------------- Run Webcam ----------------
if run:
    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    stframe = st.empty()  # placeholder for frames

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        fingertip = None
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                h, w, _ = frame.shape
                fingertip = (int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h))
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Draw stars
        for star in stars:
            color = (0, 0, 255)
            if star in selected_stars:
                color = (0, 255, 0)
            elif selected_stars and any(distance(star, sel) < NEIGHBOR_RADIUS for sel in selected_stars):
                color = (0, 255, 255)
            cv2.circle(frame, star, 12, color, -1)

        # Draw connections
        for conn in connections:
            cv2.line(frame, conn[0], conn[1], (0, 255, 0), 3)

        # Selection logic
        if fingertip:
            nearest_star = None
            min_dist = SELECTION_RADIUS
            for star in stars:
                d = distance(fingertip, star)
                if d < min_dist:
                    min_dist = d
                    nearest_star = star

            if nearest_star:
                if not selected_stars:
                    selected_stars.append(nearest_star)
                else:
                    last_selected = selected_stars[-1]
                    if nearest_star not in selected_stars and distance(last_selected, nearest_star) < NEIGHBOR_RADIUS:
                        selected_stars.append(nearest_star)
                        if (last_selected, nearest_star) not in connections and (nearest_star, last_selected) not in connections:
                            connections.append((last_selected, nearest_star))

        # Check constellation match
        for name, data in constellations.items():
            if len(selected_stars) == data["size"]:
                overlay = frame.copy()
                cv2.rectangle(overlay, (40, 60), (950, 270), (0, 0, 0), -1)
                frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)

                cv2.putText(frame, f"Constellation: {name}", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

                y0 = 150
                for i, line in enumerate(data["info"].split("\n")):
                    cv2.putText(frame, line, (50, y0 + i * 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)

        # Show frame on Streamlit
        stframe.image(frame, channels="BGR")

    cap.release()

