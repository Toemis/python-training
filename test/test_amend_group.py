# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Created'))
    app.group.modify_first_group(Group(name="amended"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header='Created'))
    app.group.modify_first_group(Group(header="group second"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer='Created'))
    app.group.modify_first_group(Group(footer="my group amended"))
