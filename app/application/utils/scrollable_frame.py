import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # 创建 Canvas 作为载体
        self.canvas = Canvas(self, bg="#F5F5F5")
        self.canvas.pack(side="left", fill="both", expand=True)

        # 设置垂直滚动条
        self.scrollbar_vert = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar_vert.set)
        self.scrollbar_vert.pack(side="right", fill="y")

        # 设置水平滚动条
        self.scrollbar_horiz = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scrollbar_horiz.set)
        self.scrollbar_horiz.pack(side="bottom", fill="x")

        # 当前显示的子框架
        self.current_child = None
        self.current_window = None

    def set_frame(self, new_frame):
        # 如果已有内容，删除旧的子框架
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None

        # 将新的框架添加到 Canvas 中
        self.current_child = new_frame
        self.current_window = self.canvas.create_window(0, 0, window=self.current_child, anchor="nw")


        self.current_child.canvas.bind("<Configure>", self._resize_scroll_region)

        
        self.scrollbar_vert.lift()
        self.scrollbar_horiz.lift()

    def _resize_scroll_region(self, event=None):
        # 设置滚动区域为所有内容的边界框
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def clear(self):
        # 清空 Canvas 中的内容
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None
            self.canvas.configure(scrollregion=(0, 0, 0, 0))
