from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name is None or other.name is None or self.name == other.name) and \
               (self.header is None or other.header is None or self.header == other.header) and \
               (self.footer is None or other.footer is None or self.footer == other.footer)

#    def __lt__(self, other):
#        return self.id < other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

