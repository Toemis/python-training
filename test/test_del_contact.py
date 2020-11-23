from model.contact import Contact
import random
import allure


def test_delete_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="New", last_name="New"))
        old_contacts = db.get_contact_list()
    with allure.step(' Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == app.contact.count()
        old_contacts.remove(contact)
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

