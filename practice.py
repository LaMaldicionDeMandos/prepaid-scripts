class Practice:
    def __init__(self, code, module, name, type, super_type, price):
        self.code = code
        self.module = module
        self.name = name
        self.type = type
        self.superType = super_type
        self.price = price

    def to_json(self):
        return '{' + f'"code": "{self.code}", "module":"{self.module}", "name":"{self.name}", "type":"{self.type}", "super_type":"{self.superType}", "price":"{self.price}"' + '}'


class PracticeCode:
    def __init__(self, code, module, name, price):
        self.code = code
        self.name = name
        self.module = module
        self.price = price
