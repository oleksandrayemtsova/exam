from lease_agreement import LeaseAgreement


class Landlord(LeaseAgreement):

    def __init__(self, tenant, landlord, name):
        super().__init__(tenant, landlord)
        self.__name = name
        self.__contract = LeaseAgreement(name)

    @property
    def name(self):
        return self.__name

    @property
    def contract(self):
        return self.__contract

    def application_for_housing(self, dwelling, tenant):
        for home in tenant.list_of_premises:
            if dwelling == home:
                self.__contract = LeaseAgreement(self.name, tenant)
                self.__contract.add_agreement(dwelling)
        else:
            print("Unfortunately, there is no such housing!")

    def __str__(self):
        return f"Name: {self.name}, Contract: {self.contract}"
