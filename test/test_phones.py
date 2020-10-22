import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)  # replace characters from first parameter


def merge_phones_like_on_home_page(contact):  # 5 - merge with '\n' between elements (using join function)
    return "\n".join(filter(lambda x: x !="",  # 4 - filter empty strings that may be created after 'clear' function
                            map(lambda x: clear(x),  # 3 - clear values from additional chars (like - or ())
                                filter(lambda x: x is not None,  # 2 - filter None values from the list below
                                       [contact.home_phone,  contact.mobile_phone,  # 1 - create a list of phones
                                        contact.work_phone, contact.phone2]))))
