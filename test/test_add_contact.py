# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10  # failed if add string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    dividers = " +-()"
    symbols = dividers + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(6, maxlen))])


def random_email():
    dividers = ["", "_", "-", "."]
    domains = ["@hotmail.com", "@gmail.com", "@rambler.ru", "@mail.ru", "@tut.by", "@yahoo.com", "@my-company.com"]
    symbols = string.ascii_lowercase + string.digits
    part1 = "".join([random.choice(symbols) for i in range(random.randrange(1, 10))])
    part2 = "".join([random.choice(symbols) for i in range(random.randrange(1, 10))])
    parts = {part1, part2}
    local = random.choice(dividers).join(parts)
    return str(local + random.choice(domains))


testdata = [
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, nickname=nickname,title=title,
            company=company, address=address,home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
            fax=fax,
                      email="toemis13@gmil.com", email2="qweqwe@test.ry", email3="asdasd@rty.by",
                      homepage="111231123.com", birth_day="5", birth_month="October",
                      birth_year="1989", aniv_day="15", aniv_month="July", aniv_year="2009",
                      address2="123123 fddfg trtrtg 555", phone2="24/3", notes="fgdg grrtthg tr")
    for first_name in ["", random_string('firstname', 15)]
    for middle_name in ["", random_string("middlename", 20)]
    for last_name in ["", random_string("lastname", 20)]
    for nickname in ["", random_string("nickname", 15)]
    for title in ["", random_string("title", 25)]
    for company in ["", random_string("company", 25)]
    for address in ["", random_string("address", 50)]
    for home_phone in ["", random_phone(20)]
    for mobile_phone in ["", random_phone(20)]
    for work_phone in ["", random_phone(20)]
    for fax in ["", random_phone(20)]





]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)