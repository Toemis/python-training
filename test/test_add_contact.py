# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import datetime


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10  # failed if add string.punctuation
    s = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    clear_string = ' '.join([t for t in s.split(' ') if t])  # delete all unnecessary additional spaces
    return clear_string


def random_phone():
    symbols = string.digits
    first_part = random.randint(100, 999)
    second_part = random.randint(1, 99)
    remaining_part = "".join([random.choice(symbols) for i in range(random.randrange(6, 20))])
    return "+%s (%s) %s" % (first_part, second_part, remaining_part)


def random_email():
    dividers = ["", "_", "-", "."]
    domains = ["@hotmail.com", "@gmail.com", "@rambler.ru", "@mail.ru", "@tut.by", "@yahoo.com", "@my-company.com"]
    symbols = string.ascii_lowercase + string.digits
    part1 = "".join([random.choice(symbols) for i in range(random.randrange(1, 10))])
    part2 = "".join([random.choice(symbols) for i in range(random.randrange(1, 10))])
    parts = {part1, part2}
    local = random.choice(dividers).join(parts)
    return str(local + random.choice(domains))


def random_url(maxlen):
    dividers = ["_", "-", "."]
    domains = [".com", ".ru", ".by", ".org"]
    symbols = string.ascii_lowercase + string.digits
    part1 = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    part2 = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
    parts = {part1, part2}
    local = random.choice(dividers).join(parts)
    return str(local + random.choice(domains))


def random_date(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    my_random_date = start_date + datetime.timedelta(days=random_number_of_days)
    date = my_random_date.strftime("%#d %B %Y").split()
    return date


testdata = [
    Contact(first_name=random_string('firstname', 15), middle_name=random_string("middlename", 20),
            last_name=random_string("lastname", 20), nickname=random_string("nickname", 15),
            title=random_string("title", 25), company=random_string("company", 25), address=random_string("address", 50),
            home_phone=random_phone(), mobile_phone=random_phone(), work_phone=random_phone(), fax=random_phone(),
            email=random_email(), email2=random_email(), email3=random_email(), homepage=random_url(15),
            birth_day=random_date(1989)[0], birth_month=random_date(1989)[1], birth_year=random_date(1989)[2],
            aniv_day=random_date(2009)[0], aniv_month=random_date(2009)[1], aniv_year=random_date(2009)[2],
            address2=random_string("address2", 55), phone2=random_phone(), notes=random_string("notes", 55))
    for i in range(3)

    # for first_name in ["", random_string('firstname', 15)]
    # for middle_name in ["", random_string("middlename", 20)]
    # for last_name in ["", random_string("lastname", 20)]
    # for nickname in ["", random_string("nickname", 15)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)