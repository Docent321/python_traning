from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
    app.contact.delete_first_contact()
