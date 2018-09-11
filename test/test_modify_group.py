
from model.group import Group
from random import randrange

def test_modify_first_groop(app):
    if app.group.count() == 0:
         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="1", header="1", footer="1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_groop_name(app):
#    if app.group.count() == 0:
#         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="New group")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_groop_header(app):
#    if app.group.count() == 0:
#         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_modify_groop_footer(app):
#    if app.group.count() == 0:
#         app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
