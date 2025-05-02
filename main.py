import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#4 da goon

root = tk.Tk()
root.title("hannah_dos")
root.geometry("600x400")
root.resizable(False, False)

bg_image = Image.open("hannah.png")
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

pink_color = "#ff69b4"
font_small = ("Comic Sans MS", 10)
font_medium = ("Comic Sans MS", 12, "bold")

header = tk.Label(root, text="hannah DoS", font=("Comic Sans MS", 16, "bold"), fg=pink_color)
header.pack(pady=8)

settings_frame = tk.Frame(root)
settings_frame.pack(pady=5)

tk.Label(settings_frame, text="target IP/domain:", font=font_small, fg=pink_color).grid(row=0, column=0, sticky="e", padx=5, pady=2)
target_entry = tk.Entry(settings_frame, font=font_small, fg=pink_color, width=20, relief="flat", highlightthickness=0, bd=0, insertbackground=pink_color)
target_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(settings_frame, text="port:", font=font_small, fg=pink_color).grid(row=1, column=0, sticky="e", padx=5, pady=2)
port_entry = tk.Entry(settings_frame, font=font_small, fg=pink_color, width=8, relief="flat", highlightthickness=0, bd=0, insertbackground=pink_color)
port_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")

tk.Label(settings_frame, text="duration (s):", font=font_small, fg=pink_color).grid(row=2, column=0, sticky="e", padx=5, pady=2)
duration_entry = tk.Entry(settings_frame, font=font_small, fg=pink_color, width=8, relief="flat", highlightthickness=0, bd=0, insertbackground=pink_color)
duration_entry.grid(row=2, column=1, padx=5, pady=2, sticky="w")

tk.Label(settings_frame, text="Attack method:", font=font_small, fg=pink_color).grid(row=3, column=0, sticky="e", padx=5, pady=2)
attack_method_var = tk.StringVar(value="UDP Flood")
attack_method_menu = tk.OptionMenu(settings_frame, attack_method_var, "UDP Flood", "SYN Flood", "HTTP Flood", "ICMP Flood")
attack_method_menu.config(font=font_small, fg=pink_color, bd=0, highlightthickness=0, activeforeground=pink_color)
attack_method_menu.grid(row=3, column=1, padx=5, pady=2, sticky="w")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

def start_attack():
    target = target_entry.get()
    port = port_entry.get()
    duration = duration_entry.get()
    method = attack_method_var.get()

   
    print(" ---- implement skidding -----")

def stop_attack():
    messagebox.showinfo("ok")

start_btn = tk.Button(button_frame, text="fuck em", command=start_attack,
                      font=font_medium, fg=pink_color, relief="flat", bd=0, highlightthickness=0, activeforeground=pink_color)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(button_frame, text="stop", command=stop_attack,
                     font=font_medium, fg=pink_color, relief="flat", bd=0, highlightthickness=0, activeforeground=pink_color)
stop_btn.grid(row=0, column=1, padx=10)

footer_label = tk.Label(root, text="github.com/JapanSturmhuhn", font=font_small, fg=pink_color)
footer_label.pack(side="bottom", pady=6)

root.mainloop()
