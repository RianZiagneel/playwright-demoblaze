from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self,page:Page, base_url:str = "https://demoblaze.com/"):
        self.page = page
        self.base_url = base_url

    def goto(self, url:str):
        self.page.goto(url)

    def get_text (self, locator:Locator) -> str:
        return locator.text_content()
    
    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator:Locator, text:str):
        locator.fill(text)
    
    def get_by_placeholder(self, placeholder:str) -> Locator:
        return self.page.get_by_placeholder(placeholder)

    def get_by_label(self, label:str) -> Locator:
        return self.page.get_by_label(label)
    
    def get_by_role(self, role:str, **kwargs) -> Locator:
        return self.page.get_by_role(role, **kwargs)
    
    def get_by_text(self, text:str) -> Locator:
        return self.page.get_by_text(text)
    
    def get_by_title(self,text:str)-> Locator:
        return self.page.get_by_title(text)
    
    def locator(self, text:str)-> Locator:
        return self.page.locator(text)
    
    def screenshot(self, path:str):
        return self.page.screenshot(path=path)