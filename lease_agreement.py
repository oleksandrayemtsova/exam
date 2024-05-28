import datetime


class LeaseAgreement:
    number_counter = 0

    def __init__(self, tenant="Sasha", landlord="Sasha"):
        self.__tenant = tenant
        self.__landlord = landlord
        self.__number = LeaseAgreement.number_counter + 1
        self.__rented_housing = []

    @property
    def tenant(self):
        return self.__tenant

    @property
    def landlord(self):
        return self.__landlord

    @property
    def number(self):
        return self.__number

    @property
    def rented_housing(self):
        return self.__rented_housing

    def add_agreement(self, dwelling):
        self.__rented_housing.append(dwelling)
        today = datetime.date.today()
        return_date = today + datetime.timedelta(days=300)
        print(return_date)

    def __str__(self):
        return f"Tenant: {self.tenant}, Landlord: {self.landlord}, Number: {self.number}, Rented housing: {self.rented_housing}"