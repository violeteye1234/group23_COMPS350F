# A testing framework for Canvas_button.py
import unittest
import tkinter as tk
from unittest.mock import Mock, patch
from canvas_button_beta import CanvasButton
#from tkinter import PhotoImage

class CanvasButtonTest(unittest.TestCase):
    def setUp(self):
        # Creating a Tkinter Window
        self.root = tk.Tk()
        # Creating a Canvas Object
        self.canvas = tk.Canvas(self.root, width=100, height=100)
        self.canvas.pack()

        # Simulating command functions
        self.mock_command = Mock()

        # Init canvasbutton and set default value
        self.button = CanvasButton(self.canvas, 50, 50, r"D:\Software Engineer 350 GP\group23_COMPS350F\app\application\utils\test_canvas_button\image_1.png", self.mock_command)

    def test_flash(self):
        # after method simulates delay
        with patch.object(self.canvas, 'after', wraps=self.canvas.after) as mock_after:
            self.button.flash()
            # Check if the button is hidden
            self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.HIDDEN)
            # Check if the after method is called
            mock_after.assert_called_with(self.button.flash_delay, self.button.set_state, tk.NORMAL)

    def test_set_state(self):
        # Set the button to hidden state
        self.button.set_state(tk.HIDDEN)
        self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.HIDDEN)

        # Set the button to normal state
        self.button.set_state(tk.NORMAL)
        self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.NORMAL)

    def tearDown(self):
        self.root.destroy()

# Running Tests
if __name__ == '__main__':
    unittest.main()