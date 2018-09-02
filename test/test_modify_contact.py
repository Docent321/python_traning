
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="1", lastname="1", address="1", home="1", email="1"))

def test_modify_contact_firtname(app):
    app.contact.modify_first_contact(Contact(firstname="firtname"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="New address"))

def test_modify_contact_home(app):
    app.contact.modify_first_contact(Contact(home="New home"))

def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="New email"))
