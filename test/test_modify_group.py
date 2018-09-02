
from model.group import Group

def test_modify_first_groop(app):
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))

def test_modify_groop_name(app):
    app.group.modify_first_group(Group(name="New group"))

def test_modify_groop_header(app):
    app.group.modify_first_group(Group(header="New header"))

def test_modify_groop_footer(app):
    app.group.modify_first_group(Group(footer="New footer"))
