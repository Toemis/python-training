import re
from model.contact import Contact


def test_home_page_vs_db_contact_info(app, db):
    home_contacts_list = app.contact.get_contact_list()
    db_contact_list = db.get_contact_list()
    db_contacts_clean = map(clean, db_contact_list)
    assert sorted(home_contacts_list, key=Contact.id_or_max) == sorted(db_contacts_clean, key=Contact.id_or_max)
    # print("db_contacts_clean:")
    # for i in list(map(clean, db_contact_list)):
    #     print(i)


# def test_contact_info_on_home_page(app):
#     home_contacts_list = app.contact.get_contact_list()
#     index = randrange(len(home_contacts_list))
#     contact_from_home_page = home_contacts_list[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.id == contact_from_edit_page.id
#     assert contact_from_home_page.first_name == contact_from_edit_page.first_name
#     assert contact_from_home_page.last_name == contact_from_edit_page.last_name
#     assert contact_from_home_page.address == clear_spaces_before_newline(contact_from_edit_page.address)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == \
#            clear_spaces_before_newline(merge_emails_like_on_home_page(contact_from_edit_page))


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_merged == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[/() -]", "", s)  # delete characters from first parameter


def clear_spaces_before_newline(s):  # maybe it's not really clear and beautiful, but it's the best what I can now
    new = ' '.join([t for t in s.split(' ') if t])  # delete all additional spaces
    new = re.sub('\\s*\\n', '\n', new)  # delete all spaces before final \n
    return new.strip()  # and unnecessary \n at the beg and end of text


def merge_phones_like_on_home_page(contact):  # 5 - merge with '\n' between elements (using join function)
    return "\n".join(filter(lambda x: x != "",  # 4 - filter empty strings that may be created after 'clear' function
                            map(lambda x: clear(x),  # 3 - clear values from additional chars (like - or ())
                                filter(lambda x: x is not None,  # 2 - filter None values from the list below
                                       [contact.home_phone, contact.mobile_phone,  # 1 - create a list of phones
                                        contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):  # create a list of emails with '\n' between them if email not None
    return "\n".join(filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))


def clean(cont):
    first_name = ' '.join(cont.first_name.split())
    last_name = ' '.join(cont.last_name.split())
    address = clear_spaces_before_newline(cont.address)
    all_phones_merged = merge_phones_like_on_home_page(cont)
    all_emails_merged = clear_spaces_before_newline(merge_emails_like_on_home_page(cont))
    # print(first_name, last_name, address, all_phones_merged, all_emails_merged)
    return Contact(id=cont.id, first_name=first_name, last_name=last_name, address=address,
                   all_phones_merged=all_phones_merged, all_emails_merged=all_emails_merged)
