# -*- coding: utf-8 -*-
from model.group import Group


def test_amend_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.amend_first_group(Group(name="amended", header="group second", footer="my group amended"))
    app.session.logout()
