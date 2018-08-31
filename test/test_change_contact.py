
from model.contact import Contact


def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact(Contact(firtname="1", lastname="1", address="1", home="1", email="1"))
    app.session.logout()