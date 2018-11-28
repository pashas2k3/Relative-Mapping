import hashlib
import operator
from datetime import datetime

class Relative(object):

    @classmethod
    def from_dict(cls, d):
        allowed_keys = ('name', 'dob', 'nickname', 'gender')
        df = {k: v for k,v in d.items() if k in allowed_keys}
        return cls(**df)

    def __init__(self, name, dob, nickname, gender):
        assert name and dob and nickname and gender
        self.name = name
        self.dob = dob
        self.nickname = nickname
        self.gender = gender

        # Calculate hash
        hash = hashlib.md5()
        hash.update(self.name.encode('utf-8'))
        hash.update(self.dob.encode('utf-8'))
        hash.update(self.nickname.encode('utf-8'))
        hash.update(self.gender.encode('utf-8'))

        self.id = hash.hexdigest()

    gender = property(operator.attrgetter('_gender'))

    @gender.setter
    def gender(self, gender):
        if gender not in ['male', 'female']:
            raise ValueError('Current recognized gender values only male or female')
        self._gender = gender

    date = property(operator.attrgetter('_date'))

    @date.setter
    def date(self, date):
        datetime.strptime(date, '%Y-%m-%d')
        self._date = date


    def asdict_attr(self):
        return {
            'name': self.name,
            'dob': self.dob,
            'nickname': self.nickname,
            'gender': self.gender}

    def asdict_key(self):
        return {
            'id': self.id
        }

    def asdict(self):
        return {**self.asdict_key(), **self.asdict_attr()}

    def __eq__(self, other):
        print(other)
        print(type(self))
        print(type(other))
        print(isinstance(other, Relative))
        if isinstance(other, Relative):
            return self.id == other.id and self.gender == other.gender and self.nickname == other.nickname \
                   and self.dob == other.dob and self.name == other.name
        return False
