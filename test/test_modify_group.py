
from model.group import Group

def test_modify_first_groop(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))

def test_modify_groop_name(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_groop_header(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.group.modify_first_group(Group(header="New header"))

def test_modify_groop_footer(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.group.modify_first_group(Group(footer="New footer"))
