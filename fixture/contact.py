from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # go to contact creation form
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.birth_day)
        self.change_dropdown_value("bmonth", contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        self.change_dropdown_value("aday", contact.aniv_day)
        self.change_dropdown_value("amonth", contact.aniv_month)
        self.change_field_value("ayear", contact.aniv_year)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_dropdown_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_xpath("//select[@name='%s']/option[text()='%s']" % (field_name, value)).click()

    #          wd.find_element_by_css_selector('select[name="%s"] > option[value="%s"]' % (field_name, value)).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def amend_first_contact(self):
        self.amend_contact_by_index(0)

    def amend_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.return_home_page()
        self.contact_cache = None

    def amend_contact_by_id(self, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(contact.id)
        # fill contact form
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.return_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for cont in wd.find_elements_by_name("entry"):
                cells = cont.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                # id = cont.find_element_by_name("selected[]").get_attribute("id")
                # last_name = cont.find_element_by_xpath("./td[2]").text
                # first_name = cont.find_element_by_xpath("./td[3]").text
                self.contact_cache.append(Contact(id=id, last_name=last_name, first_name=first_name,
                                                  all_phones_merged=all_phones,
                                                  all_emails_merged=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").text
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, phone2=phone2,
                       email=email, email2=email2, email3=email3,
                       address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone, phone2=phone2)

    def select_group_from_dropdown(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("to_group").click()
        # Select(wd.find_element_by_name("to_group")).select_by_visible_text("name xo")
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_from_dropdown(group_id)
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_group_page(group_id)
        wd.find_element_by_id("%s" % contact_id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_id("logo").click()

    def open_group_page(self, group_id):
        wd = self.app.wd
        group_url = self.app.base_url + "?group=%s" % group_id
        wd.get(group_url)



