from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    # need to clean the results from db as " " fails the test when compare with UI
    if check_ui:
        def clean(gr):
            return Group(id=gr.id, name=gr.name.strip())
        ui_groups = app.group.get_group_list()
        new_groups_clean = map(clean, db.get_group_list())
        assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)

