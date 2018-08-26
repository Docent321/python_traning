from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groops_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_groop(self, group):
        wd = self.wd
        self.open_groops_page()
        # init groop creation
        wd.find_element_by_name("new").click()
        # fill groop firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit groop creation
        wd.find_element_by_name("submit").click()
        self.return_to_groops_page()

    def return_to_groops_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_contact(self, contatc):
        wd = self.wd
        # open contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contatc.firtname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contatc.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contatc.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contatc.home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contatc.email)
        # Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.Return_contact_list()

    def Return_contact_list(self):
        wd = self.wd
        wd.find_element_by_id("logo").click()

    def destroy(self):
        self.wd.quit()

