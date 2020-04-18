class Practice:
    def __init__(self, code, name, type, super_type, price):
        self.code = code
        self.name = name
        self.type = type
        self.superType = super_type
        self.price = price

    def to_dic(self):
        return {'code': self.code, 'name': self.name, 'specialty': self.type, 'category': self.superType,
                'price': self.price}

    def to_json(self):
        return '{' + f'"code": "{self.code}", "name":"{self.name}", "type":"{self.type}", ' \
                     f'"super_type":"{self.superType}", "price":"{self.price}"' + '}'


class PracticeCode:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
