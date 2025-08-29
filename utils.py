import cv2
import math

def draw_stars(frame, stars, selected, possible):
    for i, (x,y) in enumerate(stars):
        color = (0,0,255)  # red
        if i in selected:
            color = (0,255,0)  # green
        elif i in possible:
            color = (0,255,255)  # yellow
        cv2.circle(frame, (x,y), 12, color, -1)

def draw_lines(frame, stars, selected):
    for i in range(len(selected)-1):
        cv2.line(frame, stars[selected[i]], stars[selected[i+1]], (0,255,0), 2)

def distance(p1, p2):
    return math.dist(p1, p2)

def nearby(stars, current, threshold=100):
    cx,cy = stars[current]
    return [i for i,(x,y) in enumerate(stars) if i!=current and math.dist((x,y),(cx,cy)) < threshold]
