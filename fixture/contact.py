
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # open contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.Return_contact_list()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("address", contact.address)
        self.type("home", contact.home)
        self.type("email", contact.email)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select some contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit Ok
        wd.switch_to_alert().accept()
        self.Return_contact_list()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contatc_data):
        self.modify_contact_by_index

    def modify_contact_by_index(self, index, new_contatc_data):
        wd = self.app.wd
        # submit edit
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']")[index].click()
        self.fill_contact_form(new_contatc_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.Return_contact_list()
        self.contact_cache = None

    def Return_contact_list(self):
        wd = self.app.wd
        wd.find_element_by_id("logo").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contanct_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text_lastname = element.find_elements_by_css_selector("td")[1].text
                text_firstname = element.find_elements_by_css_selector("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text_firstname, lastname=text_lastname, id=id))
        return list(self.contact_cache)

