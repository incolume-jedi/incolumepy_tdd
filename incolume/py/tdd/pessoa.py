from datetime import datetime
from unicodedata import normalize


class Pessoa:
    def __init__(self, fullname, born):
        self.fullname = fullname
        self.born = born

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, value):
        self.__fullname = self.title_name(value)

    @staticmethod
    def title_name(name: str):
        return ' '.join(
            x.title() if not (len(x) <= 3 and x.startswith('d')) else x
            for x in name.lower().split()
        )

    @property
    def firstname(self):
        return self.fullname.split()[0].title()

    @firstname.setter
    def firstname(self, value):
        fullname = self.fullname.split()
        fullname[0] = value
        self.fullname = (' '.join(fullname)).strip()

    @property
    def middlename(self):
        return ' '.join(self.fullname.split()[1:-1])

    @middlename.setter
    def middlename(self, value):
        self.fullname = '{} {} {}'.format(
            self.firstname, self.title_name(value), self.lastname
        )

    @property
    def lastname(self):
        return self.fullname.split()[-1].title()

    @lastname.setter
    def lastname(self, value):
        fullname = self.fullname.split()
        fullname[-1] = value
        self.fullname = ' '.join(fullname)

    @property
    def born(self):
        return self.__born.strftime('%d de %B de %Y')

    @born.setter
    def born(self, value):
        born = datetime.strptime(value, '%d/%m/%Y')
        self.__born = born

    def to_dict(self):
        return {
            'firstname': self.firstname,
            'middlename': self.middlename,
            'lastname': self.lastname,
            'born': self.born,
        }
