from tenant import Tenant
from landlord import Landlord
from residential_premises import ResidentialPremises


def main():
    tenant = Tenant("Oleksandra")
    landlord = Landlord("Ania")
    print(tenant)
    print(landlord)
    premises = ResidentialPremises(1, "House", 100)
    landlord.add_agreement(premises)


if __name__ == "__main__":
    main()