import operator


class Relation:
    @classmethod
    def from_dict(cls, d):
        allowed_keys = ('src', 'relation', 'dest', 'event_date')
        df = {k: v for k, v in d.items() if k in allowed_keys}
        return cls(**df)

    def __init__(self, src, relation, dest, event_date):
        # NEED OTHER VALIDATIONS
        # Spouse, Parent, Child have to have some age gaps
        # 1. Spouse has to be within 70 years
        # 2. Parent has to be older than dest by at least 12 year
        # 3. Child has to be younger than parent by at least 12 years
        if src == dest:
            raise ValueError('Cannot have cyclic relation')
        self.src = src
        self.relation = relation
        self.dest = dest
        self.event_date = event_date # Primarily for debugging

    relation = property(operator.attrgetter('_relation'))

    @relation.setter
    def relation(self, relation):
        if relation not in ('SPOUSE', 'PARENT', 'CHILD'):
            raise ValueError('Current recognized relation values are SPOUSE, PARENT, CHILD')
        self._relation = relation

    @classmethod
    def get_distance(cls, relation):
        if relation not in ('SPOUSE', 'PARENT', 'CHILD'):
            raise ValueError('Current recognized relation values are SPOUSE, PARENT, CHILD')
        return 1

    def asdict_attr(self):
        return {
            'relation': self.relation,
            'event_date': self.event_date
        }

    def asdict_key(self):
        return {
            'src': self.src,
            'dest': self.dest
        }

    def asdict(self):
        return {**self.asdict_key(), **self.asdict_attr()}
