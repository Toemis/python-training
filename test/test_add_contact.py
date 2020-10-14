# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Name", middle_name="Middle", last_name="Surname2", nickname="Toemis",
                               title="qwweqw", company="12edsdfe", address="1230009 gfhfj Rjfdkmdv; fff",
                               home="123123123", mobile="2323232323", work_phone="45455454544", fax="67676767",
                               email="toemis13@gmil.com", email2="qweqwe@test.ry", email3="asdasd@rty.by",
                               homepage="111231123.com", birth_day="5", birth_month="October",
                               birth_year="1989", aniv_day="15", aniv_month="July", aniv_year="2009",
                               address2="123123 fddfg trtrtg 555", phone2="24/3", notes="fgdg grrtthg tr")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


