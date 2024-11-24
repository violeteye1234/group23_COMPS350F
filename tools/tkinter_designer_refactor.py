import re
import os

#Define directory path
filename = r"D:\Software Engineer 350 GP\group23_COMPS350F\tkinter_designer_output\build\build\gui.py"
#filename = r"D:\Software Engineer 350 GP\group23_COMPS350F\tkinter_designer_output\build\gui.py"
# Define regular expressions and replacement patterns
patterns = [
    (r'(image_image_.*) = PhotoImage\(\s*file=relative_to_assets\((.*)\)\)', r'\1 = PhotoImage(file=relative_to_assets(\2))'),
    (r'(image_.*) = canvas.create_image\(\s*(.*),\s*(.*),\s*image=(.*)\s*\)', r'\1 = canvas.create_image(\2, \3, image=\4)'),
    (r'canvas.create_text\(\s*(.*),\s*(.*),\s*anchor=(.*),\s*text=(.*),\s*fill=(.*),\s*font=(.*)\s*\)', r'canvas.create_text(\1, \2, anchor=\3, text=\4, fill=\5, font=\6)'),
    (r'=relative_to_assets\("(.*)"\)', r'=self.image_path / "\1"'),
    (r'image_(.*) =', r'self.image_\1 ='),
    (r'=image_image_(.*)\)', r'=self.image_image_\1)'),
    (r'canvas', r'self.canvas')
]


# Process each file
if filename.endswith(".py"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace each regular expression
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write back file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

print("All files have been replaced.")
