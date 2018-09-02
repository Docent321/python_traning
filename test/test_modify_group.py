
from model.group import Group

def test_modify_first_groop(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))
    app.session.logout()

def test_modify_groop_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_groop_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()

def test_modify_groop_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="New footer"))
    app.session.logout()