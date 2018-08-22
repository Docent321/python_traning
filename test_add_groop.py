# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_groop(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groops_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_groop(self, wd):
        # init groop creation
        wd.find_element_by_name("new").click()
        # fill groop firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("qweqwe")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("qweqwe")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("qweqwe")
        # submit groop creation
        wd.find_element_by_name("submit").click()

    def return_to_groops_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_test_add_groop(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groops_page(wd)
        self.create_groop(wd)
        self.return_to_groops_page(wd)
        self.Logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
