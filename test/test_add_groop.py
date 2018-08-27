# -*- coding: utf-8 -*-
from model.group import Group

def test_add_groop(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.session.logout()

