from tkinter import *
from math import sin, cos, pi, radians
from time import localtime

root = Tk()
root.title("Analog Clock")
root.geometry("400x400")
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

cx, cy = 200, 200  # center
r = 150            # radius

def draw_clock_face():
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=4)
    for i in range(12):
        angle = radians(i * 30)
        x = cx + 0.85*r*sin(angle)
        y = cy - 0.85*r*cos(angle)
        text = str(i if i != 0 else 12)
        canvas.create_text(x, y, text=text, font=("Arial", 12, "bold"))

def draw_hand(length, angle_deg, width, color):
    angle = radians(angle_deg)
    x = cx + length*sin(angle)
    y = cy - length*cos(angle)
    return canvas.create_line(cx, cy, x, y, width=width, fill=color, tags="hands")

def update_clock():
    canvas.delete("hands")
    t = localtime()
    sec = t.tm_sec
    minute = t.tm_min + sec / 60
    hour = (t.tm_hour % 12) + minute / 60

    sec_ang = sec * 6
    min_ang = minute * 6
    hour_ang = hour * 30

    draw_hand(0.9*r, sec_ang, 1, "red")
    draw_hand(0.7*r, min_ang, 3, "blue")
    draw_hand(0.5*r, hour_ang, 5, "black")

    root.after(1000, update_clock)

draw_clock_face()
update_clock()
root.mainloop()
