from flask import Blueprint, render_template
import threading
import time
import os
import random
import pyautogui
import pyautogui as click
import requests
import pygetwindow as gw
import keyboard
import tkinter as tk
import pygame
from flask import jsonify
pyautogui.FAILSAFE = False

views = Blueprint('views', __name__)

pygame.init()


productive_sites = [
    "Google Docs", "Google Sheets", "Google Slides", "Google Drive",
    "Gmail", "Outlook", "Yahoo Mail", "Hotmail", "Microsoft Teams",
    "PyCharm", "Jupyter Notebook", "Notepad++", "Excel",
    "Word", "PowerPoint", "Terminal", "Command Prompt", "Visual Studio Code"
]
urla = "https://www.youtube.com/"
url1 = "https://www.youtube.com/watch?v=aV2RB_LiW4Y"
urls = ["https://www.twitch.tv/jynxzi","https://www.youtube.com/watch?v=KPP4Cfupzhs","https://www.tiktok.com/@jeleelyeah/video/7481041050359090478","https://www.youtube.com/watch?v=eRXE8Aebp7s","https://www.youtube.com/watch?v=72eGw4H2Ka8","https://www.youtube.com/watch?v=85z7jqGAGcc","https://www.youtube.com/watch?v=T7M3PpjBZzw"]
songs = ["https://www.youtube.com/watch?v=T6eK-2OQtew","https://www.youtube.com/watch?v=U8F5G5wR1mk"]
list_of_excuses = ["breather.mp3","chillpill.mp3","deserve.mp3","end.mp3","loadoff.mp3","overwork.mp3","relax.mp3","takeabreak.mp3"]
list_of_keys = ["alt","tab","ctrl","esc","shift","enter","backspace","space","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def findTab():
    active_window = gw.getActiveWindow()
    return active_window and any(site in active_window.title for site in productive_sites)

def procrastinate():
    def crash():
        while True:
            num1 = random.randint(1,1700)
            num2 = random.randint(1,1500)
            click.moveTo(num1,num2)
            key1 = random.choice(list_of_keys)
            key2 = random.choice(list_of_keys)
            keyboard.press_and_release(key1)
            keyboard.press_and_release(key2)
            keyboard.write(list_of_keys[random.randint(8,33)])
            click.click()
    urla = "https://www.youtube.com/"
    check1 = True
    check2 = False
    check3 = False
    while True:
        if findTab() and check1:
            print("take a break")
            pygame.mixer.init() 
            sound_path = os.path.join(os.getcwd(), "Hackathon", "website", "static", "takeabreak.mp3")
            if not os.path.exists(sound_path):
                return
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            os.system(f"start {url1}")
            time.sleep(3)
            for i in urls:
                os.system(f"start {i}")
                time.sleep(2)
            check1 = False
            check2 = True
        if findTab() and check2:
            print("Why are you still working?")
            os.system(f"start {urla}")
            
            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.overrideredirect(True) 
            root.configure(bg="black")
            root.wm_attributes("-topmost", True)  
            root.wm_attributes("-transparentcolor", "black")  
            
            def flash_text():
                current_color = label.cget("foreground")
                new_color = "red" if current_color == "black" else "black"
                label.config(foreground=new_color)
                root.after(500, flash_text) 
            
            label = tk.Label(root, text="STOP WORKING", font=("Arial", 100, "bold"), fg="red", bg="black")
            label.place(relx=0.5, rely=0.5, anchor="center")
            flash_text()
            
            root.update()
            
            
            
            sound_path = os.path.join(os.getcwd(), "Hackathon", "website", "static", "alarmSound.mp3")
            if os.path.exists(sound_path):
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(loops=-1)
            
            root.after(4000, root.destroy) 
            root.mainloop()
            

            click.click(900, 200)
            keyboard.write("subway surfers 10 hours")
            keyboard.press_and_release("enter")
            time.sleep(2)
            click.click(700, 1100)

            check2 = False
            check3 = True

        if findTab() and check3:
            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.geometry(f"{screen_width}x{screen_height}+0+0")
            root.overrideredirect(True) 
            root.wm_attributes("-topmost", True)  
            root.wm_attributes("-transparentcolor", "black")  
            canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
            canvas.pack()
            shape_size = 400  
            speed = 30  
            frame_delay = 20  
            add_shape_interval = 500  
            shapes = [] 
            colors = ["red", "blue", "green","purple", "orange", "gray23", "royal blue", "dodger blue", "salmon4", "brown4", "burlywood1", "tan2", "red4", "dark slate gray", "deep pink", "wheat4", "firebrick4", "gold", "snow4","dark orange","maroon","violet","sienna4","forest green","sea green","light sea green"]
            
            def add_new_shape():
                color = random.choice(colors)
                x, y = random.randint(0, screen_width - shape_size), random.randint(0, screen_height - shape_size)
                dx, dy = random.choice([-speed, speed]), random.choice([-speed, speed]) 
                shape = canvas.create_oval(x, y, x + shape_size, y + shape_size, fill=color, outline="")
                text = canvas.create_text(x + shape_size // 2, y + shape_size // 2, text="PROCRASTINATE", fill="white",
                                        font=("Arial", 16, "bold"))
                shapes.append((shape, text, dx, dy))
                root.after(add_shape_interval, add_new_shape)  
            
            def move_shapes():
                for i in range(len(shapes)):
                    shape, text, dx, dy = shapes[i]
                    canvas.move(shape, dx, dy)
                    canvas.move(text, dx, dy)
                    x1, y1, x2, y2 = canvas.coords(shape)
                    if x1 <= 0 or x2 >= screen_width:
                        dx = -dx
                    if y1 <= 0 or y2 >= screen_height:
                        dy = -dy
                    shapes[i] = (shape, text, dx, dy)
                root.after(frame_delay, move_shapes) 
            
            add_new_shape()
            move_shapes()
            root.after(10000, crash) 
            root.mainloop()
@views.route('/')
def home():
    return render_template("home.html")


    


@views.route('/start_procrastination', methods=['POST'])
def start_procrastination():
    threading.Thread(target=procrastinate, daemon=True).start()
    return jsonify({"message": "Procrastination started!"})

@views.route('/tiktok')
def tiktok():
    return render_template("tiktok.html", title="TikTok Doom Scroll")

@views.route('/youtube')
def youtube():
    return render_template("youtube.html", title= "Youtube Doom Scroll")

@views.route('/twitch')
def twitch():
    return render_template("shorts.html", title="Instagram Reels")

