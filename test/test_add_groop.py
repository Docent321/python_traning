# -*- coding: utf-8 -*-
from model.group import Group

def test_add_groop(app):
    app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))

