from model.group import Group
import random
import allure


def test_delete_some_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step(' Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        # need to clean the results from db as " " fails the test when compare with UI
        if check_ui:
            def clean(gr):
                return Group(id=gr.id, name=gr.name.strip())
            ui_groups = app.group.get_group_list()
            new_groups_clean = map(clean, new_groups)
            assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)
            print("UI was checked")

