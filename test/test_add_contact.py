# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        # need to clean the results from db as " " fails the test when compare with UI
        if check_ui:
            def clean(cont):
                return Contact(id=cont.id, first_name=' '.join(cont.first_name.split()),
                               last_name=' '.join(cont.last_name.split()))
            ui_contacts = app.contact.get_contact_list()
            new_contacts_clean = map(clean, new_contacts)
            assert sorted(new_contacts_clean, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)
            print("UI was checked")
