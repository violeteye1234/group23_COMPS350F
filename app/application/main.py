# main.py
from models.draggable_window import DraggableWindow
from models.logger import get_logger
import tkinter as tk

logger = get_logger()
logger.info("Application started.")

class SampleFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.name = "SampleFrame"
        label = tk.Label(self, text="Sample Frame")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Go Back", command=self.controller.go_back)
        button.pack()
        controller.logger.info("SampleFrame initialized.")
    
    def page_load(self):
        self.controller.logger.info(f"{self.name} load.")
        
    def page_update(self):
        self.controller.logger.info(f"{self.name} updated.")

if __name__ == "__main__":
    app = DraggableWindow()

    pages = [
        [               "login", LoginPage                      ],
        [       "customer_main", CustomerMainPage               ], 
        [    "customer_booking", CustomerBookingPage            ], 
        [       "customer_info", CustomerInformationPage        ], 
        ["customer_flight_info", CustomerFlightInformationPage  ],
        [          "admin_main", AdminMainPage                  ], 
        [        "admin_flight", AdminFlightTablePage           ], 
        [       "admin_booking", AdminBookingTablePage          ], 
        [       "admin_baggage", AdminBaggageTablePage          ],
        [ "admin_login_history", AdminLoginHistoryTablePage     ],
        [         "admin_admin", AdminAdminTablePage            ],
        [      "admin_customer", AdminCustomerTablePage         ],
        [      "admin_database", AdminDatabase                  ]
        ]
    
    for page in pages:
        window.add_frame(page[0], page[1])
    app.add_frame("Sample", SampleFrame)
    app.show_frame("Sample")

    app.mainloop()
    logger.info("Application closed.")
