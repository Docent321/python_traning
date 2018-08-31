
from model.group import Group

def test_change_first_groop(app):
    app.session.login(username="admin", password="secret")
    app.group.change_first_group(Group(name="1", header="1", footer="1"))
    app.session.logout()