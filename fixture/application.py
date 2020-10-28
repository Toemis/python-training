from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def return_home_page(self):
        wd = self.wd
        if not self.is_home_page():
            wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        if not self.is_home_page():
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_home_page(self):
        wd = self.wd
        return wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/addressbook/index.php")
