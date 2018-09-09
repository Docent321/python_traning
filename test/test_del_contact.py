from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="qwe", lastname="qwe", address="qwe", home="qwe", email="qwe"))
    old_contacts = app.contact.get_contanct_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contanct_list()
    assert len(old_contacts) - 1 == len(new_contacts)

