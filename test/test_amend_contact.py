# -*- coding: utf-8 -*-
from model.contact import Contact


def test_amend_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Name000")
    contact.id = old_contacts[0].id
    app.contact.amend_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_amend_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(last_name="Surname000")
    contact.id = old_contacts[0].id
    app.contact.amend_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
