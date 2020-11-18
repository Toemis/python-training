# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_one_contact_to_group(app):
    # if there are no contact/groups OR no groups without contacts create them
    if len(db.get_contact_list()) == 0 or not get_all_not_full_groups_and_contacts():
        app.contact.create(Contact(first_name="New", last_name="New"))
    if len(db.get_group_list()) == 0 or not get_all_not_full_groups_and_contacts():
        app.group.create(Group(name="test"))
    # select random group and contact not belong to it to add contact to the group
    not_paired_groups_and_contacts = get_all_not_full_groups_and_contacts()
    not_full_groups = list(not_paired_groups_and_contacts.keys())  # get the list of groups that don't have relations with contacts
    group_id = random.choice(not_full_groups)  # get random group_id from this list
    contact = not_paired_groups_and_contacts.get(group_id)[0]  # get the first contact related to this group (not in this group)
    # print(not_paired_groups_and_contacts)
    # print(group_id)
    # print(contact)
    # print(contact.id)
    group_before = list(db.get_contacts_in_group(Group(id=group_id)))
    app.contact.add_contact_to_group(contact.id, group_id)
    group_after = list(db.get_contacts_in_group(Group(id=group_id)))
    group_before.append(contact)
    assert sorted(group_before, key=Contact.id_or_max) == sorted(group_after, key=Contact.id_or_max)


def get_all_not_full_groups_and_contacts():
    all_groups = db.get_group_list()
    # create a dict with group as a key and contact that not in this group as a values
    empty_pairs = {}
    for gr in all_groups:
        if db.get_contacts_not_in_group(gr):  # if this list not empty
            empty_pairs[gr.id] = db.get_contacts_not_in_group(gr)  # add this group and contacts into the dict
    return empty_pairs

