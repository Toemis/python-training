# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_delete_one_contact_from_group(app, db, orm):
    # if there are no contact/groups create them
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="New", last_name="New"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # if there is no group-contact pair (get_all_groups_with_contacts() return empty value) create it
    if not get_all_groups_with_contacts(db, orm):
        random_contact = random.choice(db.get_contact_list())
        random_group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group(contact_id=random_contact.id, group_id=random_group.id)
    # select contact in group
    all_pairs = get_all_groups_with_contacts(db, orm)
    all_groups = list(all_pairs.keys())  # get the list of groups that have relations with contacts
    group_id = random.choice(all_groups)  # get random group_id from this list
    contact = all_pairs.get(group_id)[0]  # get the first contact related to this group
    # print(all_pairs)
    # print(group_id)
    # print(contact)
    # print(contact.id)
    group_before = list(orm.get_contacts_in_group(Group(id=group_id)))
    app.contact.delete_contact_from_group(contact.id, group_id)
    group_after = list(orm.get_contacts_in_group(Group(id=group_id)))
    group_before.remove(contact)
    assert sorted(group_before, key=Contact.id_or_max) == sorted(group_after, key=Contact.id_or_max)


def get_all_groups_with_contacts(db, orm):
    all_groups = db.get_group_list()
    # create a dict with group as a key and contacts in this group as a values
    pairs = {}
    for gr in all_groups:
        if orm.get_contacts_in_group(gr):  # if this list not empty
            pairs[gr.id] = orm.get_contacts_in_group(gr)  # add this group and contacts into the dict
    return pairs