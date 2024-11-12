import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton
from PIL import Image

class NotificationSettingPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "notification_setting/images/"
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.button_images = [tk.PhotoImage(file=self.image_path / "image_14.png"), tk.PhotoImage(file=self.image_path / "image_13.png")]
        self.current_image_index_button1 = 0
        self.current_image_index_button2 = 0
        self.current_image_index_button3 = 0
        self.current_image_index_button4 = 0
        self.current_image_index_button5 = 0
        self.current_image_index_button6 = 0
        self.current_image_index_button7 = 0
        self.current_image_index_button8 = 0
        self.current_image_index_button9 = 0

        self.button1 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button1], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button1)
        self.button1.place(x=750, y=130)
        self.button2 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button2], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button2)
        self.button2.place(x=750, y=220)
        self.button3 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button3], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button3)
        self.button3.place(x=750, y=310)
        self.button4 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button4], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button4)
        self.button4.place(x=750, y=400)
        self.button5 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button5], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button5)
        self.button5.place(x=750, y=490)
        self.button6 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button6], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button6)
        self.button6.place(x=750, y=610)
        self.button7 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button7], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button7)
        self.button7.place(x=750, y=700)
        self.button8 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button8], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button8)
        self.button8.place(x=750, y=790)
        self.button9 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button9], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button9)
        self.button9.place(x=750, y=880)
        

        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(240, 45, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_9.png")
        self.image_2 = self.canvas.create_image(420, 90, image=self.image_image_2)

        original_image_path2 = self.image_path / "image_2.png"
        desired_size2 = (850, 81)  # 期望的图片大小
        original_image2 = Image.open(original_image_path2)
        resized_image2 = original_image2.resize(desired_size2)
        resized_image2.save(original_image_path2) # 覆盖原始图片

        self.image_image_3 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_3 = self.canvas.create_image(440, 150, image=self.image_image_3)

        original_image_path3 = self.image_path / "image_3.png"
        desired_size3 = (850, 81)  # 期望的图片大小
        original_image3 = Image.open(original_image_path3)
        resized_image3 = original_image3.resize(desired_size3)
        resized_image3.save(original_image_path3) # 覆盖原始图片

        self.image_image_4 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_4 = self.canvas.create_image(440, 240, image=self.image_image_4)

        original_image_path4 = self.image_path / "image_4.png"
        desired_size4 = (850, 81)  # 期望的图片大小
        original_image4 = Image.open(original_image_path4)
        resized_image4 = original_image4.resize(desired_size4)
        resized_image4.save(original_image_path4) # 覆盖原始图片

        self.image_image_5 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_5 = self.canvas.create_image(440, 330, image=self.image_image_5)

        original_image_path5 = self.image_path / "image_5.png"
        desired_size5 = (850, 81)  # 期望的图片大小
        original_image5 = Image.open(original_image_path5)
        resized_image5 = original_image5.resize(desired_size5)
        resized_image5.save(original_image_path5) # 覆盖原始图片

        self.image_image_6 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_6 = self.canvas.create_image(440, 420, image=self.image_image_6)

        original_image_path6 = self.image_path / "image_6.png"
        desired_size6 = (850, 81)  # 期望的图片大小
        original_image6 = Image.open(original_image_path6)
        resized_image6 = original_image6.resize(desired_size6)
        resized_image6.save(original_image_path6) # 覆盖原始图片

        self.image_image_7= PhotoImage(file=self.image_path / "image_6.png")
        self.image_7 = self.canvas.create_image(440, 510, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=self.image_path / "image_10.png")
        self.image_8 = self.canvas.create_image(430, 570, image=self.image_image_8)

        original_image_path7 = self.image_path / "image_7.png"
        desired_size7 = (850, 81)  # 期望的图片大小
        original_image7 = Image.open(original_image_path7)
        resized_image7 = original_image7.resize(desired_size7)
        resized_image7.save(original_image_path7) # 覆盖原始图片

        self.image_image_9= PhotoImage(file=self.image_path / "image_7.png")
        self.image_9 = self.canvas.create_image(440, 630, image=self.image_image_9)

        original_image_path8 = self.image_path / "image_8.png"
        desired_size8 = (850, 81)  # 期望的图片大小
        original_image8 = Image.open(original_image_path8)
        resized_image8 = original_image8.resize(desired_size8)
        resized_image8.save(original_image_path8) # 覆盖原始图片

        self.image_image_10= PhotoImage(file=self.image_path / "image_8.png")
        self.image_10 = self.canvas.create_image(440, 720, image=self.image_image_10)

        original_image_path9 = self.image_path / "image_11.png"
        desired_size9 = (850, 81)  # 期望的图片大小
        original_image9 = Image.open(original_image_path9)
        resized_image9 = original_image9.resize(desired_size9)
        resized_image9.save(original_image_path9) # 覆盖原始图片

        self.image_image_11= PhotoImage(file=self.image_path / "image_11.png")
        self.image_11 = self.canvas.create_image(440, 810, image=self.image_image_11)

        original_image_path10 = self.image_path / "image_12.png"
        desired_size10 = (850, 81)  # 期望的图片大小
        original_image10 = Image.open(original_image_path10)
        resized_image10 = original_image10.resize(desired_size10)
        resized_image10.save(original_image_path10) # 覆盖原始图片

        self.image_image_12= PhotoImage(file=self.image_path / "image_12.png")
        self.image_12 = self.canvas.create_image(440, 900, image=self.image_image_12)

    def toggle_image_button1(self):
        self.current_image_index_button1 = (self.current_image_index_button1 + 1) % len(self.button_images)  # 切换图片
        self.button1.config(image=self.button_images[self.current_image_index_button1])
    def toggle_image_button2(self):
        self.current_image_index_button2 = (self.current_image_index_button2 + 1) % len(self.button_images)  # 切换图片
        self.button2.config(image=self.button_images[self.current_image_index_button2])
    def toggle_image_button3(self):
        self.current_image_index_button3 = (self.current_image_index_button3 + 1) % len(self.button_images)  # 切换图片
        self.button3.config(image=self.button_images[self.current_image_index_button3])
    def toggle_image_button4(self):
        self.current_image_index_button4 = (self.current_image_index_button4 + 1) % len(self.button_images)  # 切换图片
        self.button4.config(image=self.button_images[self.current_image_index_button4])
    def toggle_image_button5(self):
        self.current_image_index_button5 = (self.current_image_index_button5 + 1) % len(self.button_images)  # 切换图片
        self.button5.config(image=self.button_images[self.current_image_index_button5])
    def toggle_image_button6(self):
        self.current_image_index_button6 = (self.current_image_index_button6 + 1) % len(self.button_images)  # 切换图片
        self.button6.config(image=self.button_images[self.current_image_index_button6])
    def toggle_image_button7(self):
        self.current_image_index_button7 = (self.current_image_index_button7 + 1) % len(self.button_images)  # 切换图片
        self.button7.config(image=self.button_images[self.current_image_index_button7])
    def toggle_image_button8(self):
        self.current_image_index_button8 = (self.current_image_index_button8 + 1) % len(self.button_images)  # 切换图片
        self.button8.config(image=self.button_images[self.current_image_index_button8])
    def toggle_image_button9(self):
        self.current_image_index_button9 = (self.current_image_index_button9 + 1) % len(self.button_images)  # 切换图片
        self.button9.config(image=self.button_images[self.current_image_index_button9])

    def render(self):
        #button_1 = CanvasButton(self.canvas, 800, 150, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_2 = CanvasButton(self.canvas, 800, 240, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_3 = CanvasButton(self.canvas, 800, 330, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_4 = CanvasButton(self.canvas, 800, 420, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_5 = CanvasButton(self.canvas, 800, 510, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_6 = CanvasButton(self.canvas, 800, 630, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_7 = CanvasButton(self.canvas, 800, 720, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_8 = CanvasButton(self.canvas, 800, 810, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        #button_9 = CanvasButton(self.canvas, 800, 900, self.image_path / "image_14.png",
                                #lambda: self.controller.root.page_controller.switch_page(""))
        self.parent.set_frame(self)
    
    def update(self):
        pass