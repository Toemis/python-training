# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        # need to clean the results from db as " " fails the test when compare with UI
        if check_ui:
            def clean(gr):
                return Group(id=gr.id, name=gr.name.strip())
            ui_groups = app.group.get_group_list()
            new_groups_clean = map(clean, new_groups)
            assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)
            print("UI was checked")

