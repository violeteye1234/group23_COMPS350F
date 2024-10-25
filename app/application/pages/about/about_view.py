import tkinter as tk

class AboutPageView:
    def __init__(self):
        self.canvas = Canvas(window, bg = "#F5F5F5", height = 2342, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))image_1 = canvas.create_image(720.0, 38.0, image=image_image_1)
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))image_2 = canvas.create_image(128.0, 37.0, image=image_image_2)
        self.canvas.create_text(527.5, 17.0, anchor="nw", text="12:57", fill="#EBEBEB", font=("Roboto Black", 48 * -1))
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))image_3 = canvas.create_image(1348.0, 37.0, image=image_image_3)
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))image_4 = canvas.create_image(1257.0, 37.0, image=image_image_4)
        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))image_5 = canvas.create_image(1159.0, 37.0, image=image_image_5)
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))image_6 = canvas.create_image(125.0, 1208.0, image=image_image_6)
        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))image_7 = canvas.create_image(125.0, 121.0, image=image_image_7)
        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))image_8 = canvas.create_image(125.0, 261.0, image=image_image_8)
        self.image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))image_9 = canvas.create_image(125.0, 331.0, image=image_image_9)
        self.image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))image_10 = canvas.create_image(125.0, 401.0, image=image_image_10)
        self.image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))image_11 = canvas.create_image(125.0, 191.0, image=image_image_11)
        self.image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))image_12 = canvas.create_image(847.0, 220.0, image=image_image_12)
        self.canvas.create_text(322.0, 366.0, anchor="nw", text="About Us", fill="#282828", font=("Roboto Black", 48 * -1))
        self.canvas.create_text(330.0, 456.0, anchor="nw", text="Welcome to Flight Status Notification System! We are a dedicated team of professionals committed to providing top-notch services and solutions to our valued passengers. Our mission is to enhance your travel experience through innovation, reliability, and exceptional customer service.", fill="#282828", font=("Roboto Regular", 24 * -1))
        self.canvas.create_text(322.0, 630.0, anchor="nw", text="Our Team", fill="#282828", font=("Roboto Black", 48 * -1))
        self.image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))image_13 = canvas.create_image(572.0, 650.0, image=image_image_13)
        self.image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))image_14 = canvas.create_image(567.0, 845.0, image=image_image_14)
        self.image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))image_15 = canvas.create_image(1134.0, 1109.0, image=image_image_15)
        self.image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))image_16 = canvas.create_image(1134.0, 845.0, image=image_image_16)
        self.image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))image_17 = canvas.create_image(1134.0, 1373.0, image=image_image_17)
        self.image_image_18 = PhotoImage(file=relative_to_assets("image_18.png"))image_18 = canvas.create_image(567.0, 1109.0, image=image_image_18)
        self.image_image_19 = PhotoImage(file=relative_to_assets("image_19.png"))image_19 = canvas.create_image(1134.0, 1637.0, image=image_image_19)
        self.image_image_20 = PhotoImage(file=relative_to_assets("image_20.png"))image_20 = canvas.create_image(567.0, 1373.0, image=image_image_20)
        self.image_image_21 = PhotoImage(file=relative_to_assets("image_21.png"))image_21 = canvas.create_image(567.0, 1901.0, image=image_image_21)
        self.image_image_22 = PhotoImage(file=relative_to_assets("image_22.png"))image_22 = canvas.create_image(567.0, 1637.0, image=image_image_22)
        self.canvas.create_text(322.0, 2121.0, anchor="nw", text="Committed to Excellence", fill="#282828", font=("Roboto Black", 48 * -1))
        self.canvas.create_text(322.0, 2200.0, anchor="nw", text="Our team combines expertise, passion, and dedication to ensure every aspect of your journey is seamless and enjoyable. From flight tracking to personalized assistance, we are here to support you every step of the way.", fill="#282828", font=("Roboto Regular", 24 * -1))