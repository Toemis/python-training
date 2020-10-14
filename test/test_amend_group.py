# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Created'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="amended"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header='Created'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="group second"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer='Created'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="my group amended"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
