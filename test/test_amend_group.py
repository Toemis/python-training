# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_modify_group(app, db, check_ui, json_groups):
    group = json_groups     # new group data from json
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:   # create group if not exist
            app.group.create(Group(name='Created'))
        old_groups = db.get_group_list()
    with allure.step(' Given a random group from the list'):
        choose_group = random.choice(old_groups)    # select random group from old_groups
        group.id = choose_group.id      # assign it's id to the group from json
    with allure.step('When I amend the group from the list'):
        app.group.modify_group_by_id(group)
    with allure.step('Then the new group list is equal to the old list with the amended group'):
        new_groups = db.get_group_list()
        index = old_groups.index(choose_group)  # find index of amended group
        old_groups[index] = group       # change amended group to new group in the old_list
        assert old_groups == new_groups     # compare lists
        # need to clean the results from db as " " fails the test when compare with UI
        if check_ui:
            def clean(gr):
                return Group(id=gr.id, name=gr.name.strip())
            ui_groups = app.group.get_group_list()
            new_groups_clean = map(clean, new_groups)
            assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)
            print("UI was checked")