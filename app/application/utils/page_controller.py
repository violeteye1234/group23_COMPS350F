from utils.page_view import PageView

class PageController:
    def __init__(self, root, parent_container):
        self.root = root
        self.view:PageView = None
        
    def view_set_controller(self):
        self.view.set_controller(self)
    
    def render(self):
        self.view.render()
        
    def log(self, text:str) -> None:
        self.root.logger.info(text)
        
    def cleanup(self) -> None:
        self.view.destroy()
        self.view = None # type: ignore
        
    def scale_all_widgets(self, scale_factor):
        self.view.canvas.scale("all", 0, 0, scale_factor, scale_factor)  # 縮小比例
        self.view.canvas.config(scrollregion=self.view.canvas.bbox("all"))  # 更新畫布的範圍