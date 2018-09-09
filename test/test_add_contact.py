# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contanct_list()
    app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
    new_contacts = app.contact.get_contanct_list()
    assert len(old_contacts) + 1 == len(new_contacts)


