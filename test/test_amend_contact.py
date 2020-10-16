# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_amend_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Name000")
    contact.id = old_contacts[index].id
    app.contact.amend_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_amend_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(last_name="Surname000")
    contact.id = old_contacts[index].id
    app.contact.amend_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
