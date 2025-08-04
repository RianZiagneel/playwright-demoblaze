from pages.base_page import BasePage

class FrontPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.home_button = self.get_by_role("link", name="Home (current)")
        self.contact_button = self.get_by_role("link", name="Contact")
        self.contact_close_button = self.get_by_role("dialog", name="New message").get_by_label("Close")
        self.about_button = self.get_by_role("link", name="About us")
        self.close_about_button = self.locator("#videoModal").get_by_label("Close")
        self.cart_button = self.get_by_role("link", name="Cart")
        self.login_button = self.get_by_role("link", name="Log in")
        self.signup_button =  self.get_by_role("link", name="Sign up")
        self.close_login_button = self.get_by_role("dialog", name="Log in").get_by_label("Close")
        self.close_signup_button = self.get_by_role("dialog", name="Sign up").get_by_label("Close")
        self.next_button = self.locator("#next2")
        self.prev_button = self.locator("#prev2")
        self.categories = self.get_by_role("link", name="CATEGORIES")
        self.phone_categories = self.get_by_role("link", name="Phones")
        self.laptop_categories = self.get_by_role("link", name="Laptops")
        self.monitor_categories = self.get_by_role("link", name="Monitors")
        self.product_store_button = self.get_by_role("link", name="PRODUCT STORE")
        # self.goto_home = self.goto(self.base_url)

    def goto_home(self):
        return self.goto(self.base_url)



