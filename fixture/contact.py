
from model.contact import Contact
import re

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
        self.type("home", contact.homephone)
        self.type("mobile", contact.mobilephone)
        self.type("work", contact.workphone)
        self.type("phone2", contact.secondaryphone)
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
        self.modify_contact_by_index()

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

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                text_address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=text_firstname, lastname=text_lastname, id=id,
                                                  address = text_address, all_phones_from_home_page = all_phones,
                                                  all_mails_from_home_page = all_mails))
        return list(self.contact_cache)

    #список телефонов в форме редактирования
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    # список телефонов на главной странице
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return (Contact(homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, secondaryphone=secondaryphone))