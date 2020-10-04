# -*- coding: utf-8 -*-
from model.contact import Contact


def test_amend_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.amend_first_contact(Contact(first_name="Name000"))
    app.session.logout()


def test_amend_contact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.amend_first_contact(Contact(last_name="Surname000"))
    app.session.logout()
