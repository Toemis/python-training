from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
group_id = str('92')
try:
    l = db.get_contacts_in_group(Group(id=group_id))
    for item in l:
        print(item)
finally:
    pass  # db.destroy()


