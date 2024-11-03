import tkinter as tk
from tkinter import Canvas, PhotoImage
from pages.page_view import PageView

class AboutPageView(PageView):
    def __init__(self, root):
        self.canvas = Canvas(root.window, bg = "#F5F5F5", height = 2342, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(file="images/image_1.png")
        self.image_1 = self.canvas.create_image(720.0, 38.0, image=self.image_image_1)
        self.image_image_2 = PhotoImage(file="images/image_2.png")
        self.image_2 = self.canvas.create_image(128.0, 37.0, image=self.image_image_2)
        self.canvas.create_text(527.5, 17.0, anchor="nw", text="12:57", fill="#EBEBEB", font=("Roboto Black", 48 * -1))
        self.image_image_3 = PhotoImage(file="images/image_3.png")
        self.image_3 = self.canvas.create_image(1348.0, 37.0, image=self.image_image_3)
        self.image_image_4 = PhotoImage(file="images/image_4.png")
        self.image_4 = self.canvas.create_image(1257.0, 37.0, image=self.image_image_4)
        self.image_image_5 = PhotoImage(file="images/image_5.png")
        self.image_5 = self.canvas.create_image(1159.0, 37.0, image=self.image_image_5)
        self.image_image_6 = PhotoImage(file="images/image_6.png")
        self.image_6 = self.canvas.create_image(125.0, 1208.0, image=self.image_image_6)
        self.image_image_7 = PhotoImage(file="images/image_7.png")
        self.image_7 = self.canvas.create_image(125.0, 121.0, image=self.image_image_7)
        self.image_image_8 = PhotoImage(file="images/image_8.png")
        self.image_8 = self.canvas.create_image(125.0, 261.0, image=self.image_image_8)
        self.image_image_9 = PhotoImage(file="images/image_9.png")
        self.image_9 = self.canvas.create_image(125.0, 331.0, image=self.image_image_9)
        self.image_image_10 = PhotoImage(file="images/image_10.png")
        self.image_10 = self.canvas.create_image(125.0, 401.0, image=self.image_image_10)
        self.image_image_11 = PhotoImage(file="images/image_11.png")
        self.image_11 = self.canvas.create_image(125.0, 191.0, image=self.image_image_11)
        self.image_image_12 = PhotoImage(file="images/image_12.png")
        self.image_12 = self.canvas.create_image(847.0, 220.0, image=self.image_image_12)
        self.canvas.create_text(322.0, 366.0, anchor="nw", text="About Us", fill="#282828", font=("Roboto Black", 48 * -1))
        self.canvas.create_text(330.0, 456.0, anchor="nw", text="Welcome to Flight Status Notification System! We are a dedicated team of professionals committed to providing top-notch services and solutions to our valued passengers. Our mission is to enhance your travel experience through innovation, reliability, and exceptional customer service.", fill="#282828", font=("Roboto Regular", 24 * -1))
        self.canvas.create_text(322.0, 630.0, anchor="nw", text="Our Team", fill="#282828", font=("Roboto Black", 48 * -1))
        self.image_image_13 = PhotoImage(file="images/image_13.png")
        self.image_13 = self.canvas.create_image(572.0, 650.0, image=self.image_image_13)
        self.image_image_14 = PhotoImage(file="images/image_14.png")
        self.image_14 = self.canvas.create_image(567.0, 845.0, image=self.image_image_14)
        self.image_image_15 = PhotoImage(file="images/image_15.png")
        self.image_15 = self.canvas.create_image(1134.0, 1109.0, image=self.image_image_15)
        self.image_image_16 = PhotoImage(file="images/image_16.png")
        self.image_16 = self.canvas.create_image(1134.0, 845.0, image=self.image_image_16)
        self.image_image_17 = PhotoImage(file="images/image_17.png")
        self.image_17 = self.canvas.create_image(1134.0, 1373.0, image=self.image_image_17)
        self.image_image_18 = PhotoImage(file="images/image_18.png")
        self.image_18 = self.canvas.create_image(567.0, 1109.0, image=self.image_image_18)
        self.image_image_19 = PhotoImage(file="images/image_19.png")
        self.image_19 = self.canvas.create_image(1134.0, 1637.0, image=self.image_image_19)
        self.image_image_20 = PhotoImage(file="images/image_20.png")
        self.image_20 = self.canvas.create_image(567.0, 1373.0, image=self.image_image_20)
        self.image_image_21 = PhotoImage(file="images/image_21.png")
        self.image_21 = self.canvas.create_image(567.0, 1901.0, image=self.image_image_21)
        self.image_image_22 = PhotoImage(file="images/image_22.png")
        self.image_22 = self.canvas.create_image(567.0, 1637.0, image=self.image_image_22)
        self.canvas.create_text(322.0, 2121.0, anchor="nw", text="Committed to Excellence", fill="#282828", font=("Roboto Black", 48 * -1))
        self.canvas.create_text(322.0, 2200.0, anchor="nw", text="Our team combines expertise, passion, and dedication to ensure every aspect of your journey is seamless and enjoyable. From flight tracking to personalized assistance, we are here to support you every step of the way.", fill="#282828", font=("Roboto Regular", 24 * -1))
        
    def render(self):
        pass
    
    def update(self):
        pass