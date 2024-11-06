import re
import os

# 定義目錄路徑
filename = r"D:\Software Engineer 350 GP\group23_COMPS350F\tkinter_designer_output\build\build\gui.py"
#filename = r"D:\Software Engineer 350 GP\group23_COMPS350F\tkinter_designer_output\build\gui.py"
# 定義正則表達式和替換模式
patterns = [
    (r'(image_image_.*) = PhotoImage\(\s*file=relative_to_assets\((.*)\)\)', r'\1 = PhotoImage(file=relative_to_assets(\2))'),
    (r'(image_.*) = canvas.create_image\(\s*(.*),\s*(.*),\s*image=(.*)\s*\)', r'\1 = canvas.create_image(\2, \3, image=\4)'),
    (r'canvas.create_text\(\s*(.*),\s*(.*),\s*anchor=(.*),\s*text=(.*),\s*fill=(.*),\s*font=(.*)\s*\)', r'canvas.create_text(\1, \2, anchor=\3, text=\4, fill=\5, font=\6)'),
    (r'=relative_to_assets\("(.*)"\)', r'=self.image_path / "\1"'),
    (r'image_(.*) =', r'self.image_\1 ='),
    (r'=image_image_(.*)\)', r'=self.image_image_\1)'),
    (r'canvas', r'self.canvas')
]


# 處理每個文件
if filename.endswith(".py"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 對每個正則表達式進行替換
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # 寫回文件
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

print("所有文件已完成替換處理。")
