from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        first_name = Optional(str, column="firstname")
        last_name = Optional(str, column="lastname")
        email = Optional(str, column="email")
        address = Optional(str, column="address")
        home_phone = Optional(str, column="home")
        mobile_phone = Optional(str, column="mobile")
        work_phone = Optional(str, column="work")
        phone2 = Optional(str, column="phone2")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.first_name, last_name=contact.last_name, email=contact.email)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def get_orm_group_by_id(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_orm_group_by_id(group)
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_orm_group_by_id(group)
        return self.convert_contacts_to_model\
            (select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))



