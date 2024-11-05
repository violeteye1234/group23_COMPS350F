import tkinter as tk

class ResizableCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.original_width = kwargs.get('width', 1440)
        self.original_height = kwargs.get('height', 2342)

    def on_resize(self, event):
        # 計算縮放比例
        scale_x = event.width / self.original_width
        scale_y = event.height / self.original_height

        # 更新 Canvas 的尺寸
        self.config(width=event.width, height=event.height)

        # 縮放所有物件
        self.scale("all", 0, 0, scale_x, scale_y)

        # 更新原始尺寸
        self.original_width = event.width
        self.original_height = event.height