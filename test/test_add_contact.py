# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contanct_list()
    contact = Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe")
    app.contact.create(contact)
    new_contacts = app.contact.get_contanct_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


