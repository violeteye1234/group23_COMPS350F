from pages.page_view import PageView

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