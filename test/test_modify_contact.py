
from model.contact import Contact
from random import randrange

#def test_modify_first_contact(app):
#    if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
#    old_contacts = app.contact.get_contanct_list()
#    app.contact.modify_first_contact(Contact(firstname="1", lastname="1", address="1", home="1", email="1"))
#    new_contacts = app.contact.get_contanct_list()
#    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_contact(app):
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
    old_contacts = app.contact.get_contanct_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="2", lastname="2", address="1", home="1", email="1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contanct_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
#    app.contact.modify_first_contact(Contact(lastname="New lastname"))

#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
#    app.contact.modify_first_contact(Contact(address="New address"))

#def test_modify_contact_home(app):
#    if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
#    app.contact.modify_first_contact(Contact(home="New home"))

#def test_modify_contact_email(app):
#    if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
#    app.contact.modify_first_contact(Contact(email="New email"))
