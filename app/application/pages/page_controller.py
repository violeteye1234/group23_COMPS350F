from pages.page_view import PageView

class PageController:
    def __init__(self, root):
        self.root = root
        self.view:PageView = None
        
    def view_set_controller(self):
        self.view.set_controller(self)
    
    def render(self):
        self.view.render()