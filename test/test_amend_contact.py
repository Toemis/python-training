# -*- coding: utf-8 -*-
from model.contact import Contact


def test_amend_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    app.contact.amend_first_contact(Contact(first_name="Name000"))


def test_amend_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    app.contact.amend_first_contact(Contact(last_name="Surname000"))
