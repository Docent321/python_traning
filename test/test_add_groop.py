# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_groop(app):
    app.login(username="admin", password="secret")
    app.create_groop(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.logout()

