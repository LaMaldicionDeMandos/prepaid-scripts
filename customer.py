class HealthEntity:
    def __init__(self, entity_type, business_name, fantasy_name, last_name, first_name, enrollment, specialties,
                 practices,
                 province, city, town, address_street, address_number, address_floor, address_flat, phone, email):
        self.entity_type = entity_type
        self.business_name = business_name
        self.fantasy_name = fantasy_name
        self.last_name = last_name
        self.first_name = first_name
        self.enrollment = enrollment
        self.specialties = specialties
        self.practices = practices
        self.province = province
        self.city = city
        self.town = town
        self.address_street = address_street
        self.address_number = address_number
        self.address_floor = address_floor
        self.address_flat = address_flat
        self.phone = phone
        self.email = email

    def to_dic(self):
        return {'entity_type': self.entity_type, 'business_name': self.business_name, 'fantasy_name': self.fantasy_name,
                'last_name': self.last_name, 'first_name': self.first_name, 'enrollment': self.enrollment,
                'specialties': self.specialties, 'practices': self.practices, 'province': self.province,
                'city': self.city, 'town': self.town, 'address_street': self.address_street,
                'address_number': self.address_number, 'address_floor': self.address_floor,
                'address_flat': self.address_flat, 'phone': self.phone, 'email': self.email}

    def to_json(self):
        return '{' + f'"entity_type": "{self.entity_type}", "business_name":"{self.business_name}", ' \
                     f'"fantasy_name":"{self.fantasy_name}", "last_name":"{self.last_name}", ' \
                     f'"first_name":"{self.first_name}", "enrollment":"{self.enrollment}", ' \
                     f'"specialties":"{self.specialties}", "practices":"{self.practices}", ' \
                     f'"provinces":"{self.province}", "city":"{self.city}", ' \
                     f'"town":"{self.town}", "address_street":"{self.address_street}", ' \
                     f'"address_number":"{self.address_number}", "address_floor":"{self.address_floor}", ' \
                     f'"address_flat":"{self.address_flat}", "phone":"{self.phone}", ' \
                     f'"email":"{self.email}"' + '}'
