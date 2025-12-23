class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number= phone_number

    def to_dict(self):
        contact = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }
        return contact