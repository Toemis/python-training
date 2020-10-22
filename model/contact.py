from sys import maxsize

class Contact:
    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, birth_day=None, birth_month=None, birth_year=None, aniv_day=None, aniv_month=None,
                 aniv_year=None, address2=None, phone2=None, notes=None, all_phones_from_home_page=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.aniv_day = aniv_day
        self.aniv_month = aniv_month
        self.aniv_year = aniv_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s, last_name: %s, first_name: %s" % (self.id, self.last_name, self.first_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.last_name is None or other.last_name is None or self.last_name == other.last_name) and \
               (self.first_name is None or other.first_name is None or self.first_name == other.first_name)




