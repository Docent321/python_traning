from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", homephone="homephone1", email="email1",
            email2="email21", email3="email31", mobilephone="mobilephone1",workphone="workphone1", secondaryphone="secondaryphone1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", homephone="homephone2", email="email2",
            email2="email22", email3="email33", mobilephone="mobilephone2",workphone="workphone2", secondaryphone="secondaryphone2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", email="", mobilephone="",workphone="", secondaryphone="")] + \
           [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 10), homephone=random_string("homephone", 10),
            email=random_string("email", 10), mobilephone=random_string("mobilephone", 10),
            workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10))
    for i in range(5)
    ]
