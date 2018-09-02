

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groops_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groops_page()
        # init groop creation
        wd.find_element_by_name("new").click()
        self.fill_group_firm(group)
        # submit groop creation
        wd.find_element_by_name("submit").click()
        self.return_to_groops_page()

    def fill_group_firm(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groops_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groops_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_first_group(self, group):
        wd = self.app.wd
        self.open_groops_page()
        self.select_first_group()
        # submit edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_firm(group)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groops_page()


    def return_to_groops_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

