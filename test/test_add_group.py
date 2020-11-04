# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # need to clean the results from db as " " fails the test when compare with UI
    if check_ui:
        def clean(gr):
            return Group(id=gr.id, name=gr.name.strip())
        ui_groups = app.group.get_group_list()
        new_groups_clean = map(clean, db.get_group_list())
        assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)

