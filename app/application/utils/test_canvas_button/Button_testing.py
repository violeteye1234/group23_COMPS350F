# A testing framework for Canvas_button.py

import unittest
import tkinter as tk
from unittest.mock import Mock, patch
from canvas_button_bata import CanvasButton
#from tkinter import PhotoImage

class CanvasButtonTest(unittest.TestCase):
    def setUp(self):
        # 创建Tkinter窗口
        self.root = tk.Tk()
        # 创建Canvas对象
        self.canvas = tk.Canvas(self.root, width=100, height=100)
        self.canvas.pack()

        # mock the command function
        self.mock_command = Mock()

        # init canvasbutton       default
        #self.image_path = self.image_path / "login_groundstaff/images/"
        #self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        #self.button = CanvasButton(self.canvas, 50, 50, self.image_image_1, self.mock_command)
        self.button = CanvasButton(self.canvas, 50, 50, r"D:\Software Engineer 350 GP\group23_COMPS350F\app\application\utils\test_canvas_button\image_1.png", self.mock_command)

    def test_flash(self):
        # Patch the after method to simulate the delay
        with patch.object(self.canvas, 'after', wraps=self.canvas.after) as mock_after:
            self.button.flash()
            # 检查button是否隐藏
            self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.HIDDEN)
            # 检查after方法是否被调用
            mock_after.assert_called_with(self.button.flash_delay, self.button.set_state, tk.NORMAL)

    def test_set_state(self):
        # 设置按钮为隐藏状态
        self.button.set_state(tk.HIDDEN)
        self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.HIDDEN)

        # 设置按钮为正常状态
        self.button.set_state(tk.NORMAL)
        self.assertEqual(self.canvas.itemcget(self.button.canvas_btn_img_obj, 'state'), tk.NORMAL)

    def tearDown(self):
        self.root.destroy()

# 运行测试
if __name__ == '__main__':
    unittest.main()