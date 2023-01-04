import tkinter as tk
from PIL import Image, ImageTk
import customtkinter


class App:
    def __init__(self):
        
        self.all_frame = tk.Tk()
        self.root = customtkinter.CTkFrame(self.all_frame)
        self.root.grid(row=0, column=0, padx=2, pady=2)

        self.label = tk.Label(self.root, text="Roll-Pitch")
        self.label.grid(row=0, column=0, pady=4, padx=4)
        self.canvas_frame = customtkinter.CTkFrame(self.root)
        self.canvas_frame.grid(row=1, column=0, padx=2, pady=2, columnspan=2, sticky="nsew")
        
        self.canvas = tk.Canvas(self.canvas_frame, width=200, height=200)
        self.canvas.grid(row=0, column=0, pady=4, padx=4)
        self.canvas.pack()

        self.image1 = Image.open("RPY.png")
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.image2 = Image.open("vehicle.png")
        self.image2 = ImageTk.PhotoImage(self.image2)

        self.image1_id = self.canvas.create_image(100, 100, image=self.image1, tag='image')
        self.image2_id = self.canvas.create_image(100, 100, image=self.image2, tag='circle')
        self.circle_id = self.canvas.create_oval(200, 200, 5, 5, outline='black', width=2, fill='', tag='circle')
        self.circle_id_2 = self.canvas.create_oval(250, 250, -45, -45, outline='black', width=80, fill='', tag='circle')
        
        self.label_2 = tk.Label(self.root, text="Pitch")
        self.label_2.grid(row=0, column=2, pady=4, padx=4)
        self.slider_pitch = customtkinter.CTkSlider(master=self.root, command=lambda angle_p: self.pitch_f(), from_=-1, to=1, width=15, orientation="vertical")
        self.slider_pitch.grid(row=1, column=2, pady=2, padx=4, sticky="ns", rowspan=2)
        self.slider_pitch.set(0)
        self.label_3 = tk.Label(self.root, text="Roll")
        self.label_3.grid(row=5, column=2, pady=4, padx=4)
        self.slider_roll = customtkinter.CTkSlider(master=self.root, command=lambda angle: self.roll_f(), from_=-90, to=90, width=250)
        self.slider_roll.grid(row=5, column=0, pady=4, padx=2, sticky="se", columnspan=2)
        self.slider_roll.set(0.5)
        
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.angle = 0
        self.canvas.tag_lower('image')
        
    def roll_f(self):
        self.roll_value = self.slider_roll.get()
        image = Image.open("RPY.png")
        self.rotated_image = image.rotate(self.roll_value, expand=1)
        self.image1 = ImageTk.PhotoImage(self.rotated_image)
        
        self.image1_id = self.canvas.create_image(100, 100, image=self.image1, tag='image')
        self.canvas.pack(anchor=tk.CENTER, expand=True)
        self.pitch_f()
        self.canvas.tag_lower('image')
        
    def pitch_f(self):
        self.pitch_value = self.slider_pitch.get()
        # Calculate the new position of the image
        x = 100
        y = 100 + 50 * self.pitch_value
        # Update the position of the image
        self.canvas.coords(self.image1_id, x, y)
        self.canvas.tag_lower('image')
               

app = App()
app.root.mainloop()
