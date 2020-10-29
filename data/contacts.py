# -*- coding: utf-8 -*-
from model.contact import Contact


testdata = [
    Contact(first_name='firstname1', middle_name="middlename1", last_name="lastname1",
            mobile_phone="123 113 444", email="toemi@web.com", birth_day="5", birth_month="October", birth_year="1989"),
    Contact(first_name='firstname2', middle_name="middlename2", last_name="lastname2",
            mobile_phone="555 00 00", email="bio@web.com", aniv_day="4", aniv_month="July", aniv_year="2009")
]