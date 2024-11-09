import tkinter as tk
from utils.page_view import PageView

class BaggageDetailPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        
        self.baggage_info_label = tk.Label(self.canvas, text="", bg="#F5F5F5", font=("Roboto", 14))
        self.baggage_info_label.place(x=20, y=100)

    def render(self, baggage):
        self.canvas.create_text(69, 32, anchor="nw", text="Baggage Detail", fill="#282828", font=("Roboto Black", 36 * -1))
        self.update_baggage_info(baggage)
        self.parent.set_frame(self)

    def update_baggage_info(self, baggage):
        info = (
            f"ID: {baggage.baggage_id}\n"
            f"User ID: {baggage.user_id}\n"
            f"Flight Number: {baggage.flight_number}\n"
            f"Status: {baggage.status}\n"
            f"Current Location: {baggage.current_location}\n"
            f"Activity History: {baggage.activity_history}"
        )
        self.baggage_info_label.config(text=info)

    def update(self):
        pass