class HealthEntity:
    def __init__(self, entity_type, business_name, fantasy_name, name, enrollment, categories, specialties, practices, province,
                 city, town, address, phone, email):
        self.entity_type = entity_type
        self.business_name = business_name
        self.fantasy_name = fantasy_name
        self.name = name
        self.enrollment = enrollment
        self.categories = categories
        self.specialties = specialties
        self.practices = practices
        self.province = province
        self.city = city
        self.town = town
        self.address = address
        self.phone = phone
        self.email = email

    def to_dic(self):
        return {'entity_type': self.entity_type, 'business_name': self.business_name, 'fantasy_name': self.fantasy_name,
                'name': self.name, 'enrollment': self.enrollment, 'categories': self.categories,
                'specialties': self.specialties, 'practices': self.practices, 'province': self.province,
                'city': self.city, 'town': self.town, 'address': self.address, 'phone': self.phone,'email': self.email}

    def to_json(self):
        return '{' + f'"entity_type": "{self.entity_type}", "business_name":"{self.business_name}", ' \
                     f'"fantasy_name":"{self.fantasy_name}", ' \
                     f'"name":"{self.name}", "enrollment":"{self.enrollment}", ' \
                     f'"categories":"{self.categories}", "specialties":"{self.specialties}", "practices":"{self.practices}", ' \
                     f'"provinces":"{self.province}", "city":"{self.city}", ' \
                     f'"town":"{self.town}", "address":"{self.address}", ' \
                     f'"phone":"{self.phone}", ' \
                     f'"email":"{self.email}"' + '}'
