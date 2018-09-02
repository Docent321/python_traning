
from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="1", lastname="1", address="1", home="1", email="1"))
    app.session.logout()

def test_modify_contact_firtname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="firtname"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    app.session.logout()

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="New address"))
    app.session.logout()

def test_modify_contact_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home="New home"))
    app.session.logout()

def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="New email"))
    app.session.logout()