
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
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit Ok
        wd.switch_to_alert().accept()
        self.Return_contact_list()

    def modify_first_contact(self, new_contatc_data):
        wd = self.app.wd
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contatc_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.Return_contact_list()

    def Return_contact_list(self):
        wd = self.app.wd
        wd.find_element_by_id("logo").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contanct_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts

