import tkinter as tk
from tkinter import colorchooser

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

def update_color(event=None):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()
    color = f"#{red:02x}{green:02x}{blue:02x}"
    color_label.config(text=color)
    color_box.config(bg=color)

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        red_slider.set(int(color[1:3], 16))
        green_slider.set(int(color[3:5], 16))
        blue_slider.set(int(color[5:7], 16))
        update_color()

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Advanced Color Picker")
root.geometry("1240x920")
root.attributes("-alpha", 0.9)
root.overrideredirect(True)

# Center the window on the screen
center_window(root)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

red_label = tk.Label(main_frame, text="Red")
red_label.pack()
red_slider = tk.Scale(main_frame, from_=0, to=255, orient="horizontal", command=update_color)
red_slider.pack()

green_label = tk.Label(main_frame, text="Green")
green_label.pack()
green_slider = tk.Scale(main_frame, from_=0, to=255, orient="horizontal", command=update_color)
green_slider.pack()

blue_label = tk.Label(main_frame, text="Blue")
blue_label.pack()
blue_slider = tk.Scale(main_frame, from_=0, to=255, orient="horizontal", command=update_color)
blue_slider.pack()

color_label = tk.Label(main_frame, text="Pick a color", font=("Arial", 20))
color_label.pack(pady=20)

color_box = tk.Label(main_frame, width=20, height=5, relief="solid")
color_box.pack(pady=10)

color_button = tk.Button(main_frame, text="Choose Color", command=choose_color)
color_button.pack(pady=10)

quit_button = tk.Button(main_frame, text="Quit", command=quit_app)
quit_button.pack(side="bottom", pady=20)

root.mainloop()
