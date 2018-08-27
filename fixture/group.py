

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
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
