import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        #Create Canvas as a carrier
        self.canvas = Canvas(self, bg="#F5F5F5")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Set vertical scroll bar
        self.scrollbar_vert = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar_vert.set)
        self.scrollbar_vert.pack(side="right", fill="y")

        # Bind wheel event
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # The currently displayed subframe
        self.current_child = None
        self.current_window = None

    def set_frame(self, new_frame):
        # Delete old subframe if content already exists
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None

        # Add new frames to Canvas
        self.current_child = new_frame
        self.current_window = self.canvas.create_window(0, 0, window=self.current_child, anchor="nw")

        self.current_child.bind("<Configure>", self._resize_scroll_region)

        self.scrollbar_vert.lift()

    def _resize_scroll_region(self, event=None):
        # Set the scroll area to the bounding box of all content
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        # Mouse wheel scroll event, adjust scroll step size
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def clear(self):
        # Clear the contents of the Canvas
        if self.current_child:
            self.canvas.delete(self.current_window)
            self.current_child.destroy()
            self.current_child = None
            self.canvas.configure(scrollregion=(0, 0, 0, 0))
