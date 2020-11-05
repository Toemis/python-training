# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import random


def test_amend_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = db.get_contact_list()
    choose_contact = random.choice(old_contacts)
    contact.id = choose_contact.id
    app.contact.amend_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(choose_contact)
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    # need to clean the results from db as " " fails the test when compare with UI
    if check_ui:
        def clean(cont):
            return Contact(id=cont.id, first_name=' '.join(cont.first_name.split()),
                           last_name=' '.join(cont.last_name.split()))

        ui_contacts = app.contact.get_contact_list()
        new_contacts_clean = map(clean, new_contacts)
        assert sorted(new_contacts_clean, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)
        print("UI was checked")


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_amend_contact_last_name(app, contact):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="New", last_name="New"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(last_name="Surname000")
#     contact.id = old_contacts[index].id
#     app.contact.amend_contact_by_index(contact, index)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
