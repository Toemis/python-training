# -*- coding: utf-8 -*-
from application import Application

import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="new1", header="group first", footer="my group"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
