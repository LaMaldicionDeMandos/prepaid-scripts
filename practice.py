class Practice:
    def __init__(self, code, name, type, superType, price):
        self.code = code
        self.name = name
        self.type = type
        self.superType = superType
        self.price = price

    def toJson(self):
        return '{' + f'"code": "{self.code}", "name":"{self.name}", "type":"{self.type}", "super_type":"{self.superType}", "price":"{self.price}"' + '}'
