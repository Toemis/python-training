# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="amended"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="group second"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="my group amended"))
