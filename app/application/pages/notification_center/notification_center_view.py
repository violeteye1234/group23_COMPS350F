import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image
#from utils.scrollable_frame import ScrollableFrame

class NotificationCenterPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "notification_center/images/"
        self.canvas = tk.Canvas(self, bg="#F5F5F5", height=712.5, width=892.5, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)        
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        original_image_path2 = self.image_path / "image_2.png"
        desired_size2 = (800, 100)  # 期望的图片大小
        original_image2 = Image.open(original_image_path2)
        resized_image2 = original_image2.resize(desired_size2)
        resized_image2.save(original_image_path2) # 覆盖原始图片

        original_image_path3 = self.image_path / "image_3.png"
        desired_size3 = (800, 100)  # 期望的图片大小
        original_image3 = Image.open(original_image_path3)
        resized_image3 = original_image3.resize(desired_size3)
        resized_image3.save(original_image_path3) # 覆盖原始图片
       
        MYBAGGAGE_check = f"Your Baggage is checking at {self.controller.one_hour_ago}                                                                        There is half an hour before boarding.                                                                         Please go through security as soon as possible."
        MYBAGGAGE_arrive =f"Your Baggage arrived at {self.controller.a_quarter_later}                                                                                                    Please pick it up as soon as possible"
        MYFLIGHT_boarding = f"Your Flight is boarding at {self.controller.half_hour_ago}                                                                                                    Please board the plane as soon as possible" 

        if self.controller.time_until_takeoff > 60 or self.controller.time_until_takeoff < 0 or self.controller.time_later_landing < 0:
            i = 2
        elif self.controller.time_until_takeoff <= 60 and self.controller.time_until_takeoff > 30:
    # 代码块，处理时间介于30到60分钟之间的情况
            i = 1
        elif self.controller.time_until_takeoff <= 30 and self.controller.time_until_takeoff > 0:
    # 代码块，处理时间介于0到30分钟之间的情况
            i = 2
        if self.controller.time_later_landing >= 15:
    # 处理时间大于等于15分钟的情况
            i= 3

        if i == 0:
            label = tk.Label(self.canvas, text="No messages", font=("Arial", 16), bg="#F5F5F5")
            label.place(x=420, y=120)
        elif i == 1:
            button1 = CanvasButton(self.canvas, 420,120, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                      self.image_path / "image_2.png",text=MYBAGGAGE_check, font_size=16)
        elif i == 2:
            button1 = CanvasButton(self.canvas, 420,220, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                      self.image_path / "image_2.png",text=MYBAGGAGE_check, font_size=16)

            button2 = CanvasButton(self.canvas,420,120, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_flight"),
                                      self.image_path / "image_2.png",text=MYFLIGHT_boarding, font_size=16)
        if i == 3:
            button1 = CanvasButton(self.canvas, 420,320, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                      self.image_path / "image_2.png",text=MYBAGGAGE_check, font_size=16)

            button2 = CanvasButton(self.canvas,420,220, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_flight"),
                                      self.image_path / "image_2.png",text=MYFLIGHT_boarding, font_size=16)

            button3 = CanvasButton(self.canvas, 420,120, self.image_path / "image_3.png",
                                      lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                      self.image_path / "image_2.png",text=MYBAGGAGE_arrive, font_size=16)
        
        self.parent.set_frame(self)

        

    def update(self):
        pass