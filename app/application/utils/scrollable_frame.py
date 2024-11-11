import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # 創建 Canvas 作为載體
        self.canvas = Canvas(self, bg="#F5F5F5")
        self.canvas.pack(side="left", fill="both", expand=True)

        # 設置垂直滾動條
        self.scrollbar_vert = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar_vert.set)
        self.scrollbar_vert.pack(side="right", fill="y")

        # 綁定滾輪事件
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # 當前顯示的子框架
        self.current_child = None
        self.current_window = None

    def set_frame(self, new_frame):
        # 如果已有內容，刪除舊的子框架
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None

        # 將新的框架添加到 Canvas 中
        self.current_child = new_frame
        self.current_window = self.canvas.create_window(0, 0, window=self.current_child, anchor="nw")

        self.current_child.bind("<Configure>", self._resize_scroll_region)

        self.scrollbar_vert.lift()

    def _resize_scroll_region(self, event=None):
        # 設置滾動區域為所有內容的邊界框
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        # 鼠標滾輪滾動事件，調整滾動步長
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def clear(self):
        # 清空 Canvas 中的內容
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None
            self.canvas.configure(scrollregion=(0, 0, 0, 0))
