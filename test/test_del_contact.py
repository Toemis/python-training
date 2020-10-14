from selenium.common.exceptions import StaleElementReferenceException

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) - 1 == len(new_contacts)


