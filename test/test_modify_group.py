
from model.group import Group

def test_modify_first_groop(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="1", header="1", footer="1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_groop_name(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_groop_header(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_groop_footer(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
