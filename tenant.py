from residential_premises import ResidentialPremises

premises1 = ResidentialPremises(5, "Apartment", 200)
premises2 = ResidentialPremises(2, "Apartment", 700)
premises3 = ResidentialPremises(1, "House", 100)
list = [premises1, premises2, premises3]


class Tenant(ResidentialPremises):

    def __init__(self, floor, type, area, name):
        super().__init__(floor, type, area)
        self.__name = name
        self.__list_of_premises = Tenant.list

    @property
    def name(self):
        return self.__name

    @property
    def list_of_premises(self):
        for item in self.__list_of_premises:
            print(item)
        return "Residential premises with a landlord"

    def __str__(self):
        return f"Name: {self.name}, List of premises: {self.list_of_premises}"
