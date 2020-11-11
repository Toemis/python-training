import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, "
                           "email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, address, home, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), first_name=first_name, last_name=last_name, address=address,
                                            home_phone=home, mobile_phone=mobile, work_phone=work, phone2=phone2,
                                            email=email, email2=email2, email3=email3, all_phones_merged=None,
                                            all_emails_merged=None))

                # email = email, email2 = email2, email3 = email3, all_phones_merged = "/n".join(
                #     filter(lambda x: x is not None, [home, mobile, work, phone2])),
                # all_emails_merged = "/n".join(filter(lambda x: x is not None,
                #                                      [email, email2, email3]))))

        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()