# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10  # failed if add string.punctuation
    s = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    clear_string = ' '.join([t for t in s.split(' ') if t])  # delete all unnecessary additional spaces
    return clear_string


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name='Created'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
