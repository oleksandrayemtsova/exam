class ResidentialPremises:
    name_type = {"Apartment", "House"}

    def __init__(self, floor=1, type="Apartment", area=200):
        self.__floor = floor
        self.__type = type
        self.__area = area

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        if type(floor) == int:
            self.__floor = floor
        else:
            print("Floor must be an integer!")

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        if type(type) == int:
            self.__type = type
        else:
            print("Floor must be an integer!")

    @type.setter
    def type(self, type):
        if type(type) == str:
            for i in ResidentialPremises.name_type:
                if type == i:
                    self.__type = type
                    break
            else:
                print("Invalid type")
        else:
            print("Type must be a string!")

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        if type(area) == int:
            if area > 0:
                self.__area = area
            else:
                print("Invalid area")
        else:
            print("Area must be an integer!")

    def __str__(self):
        return f"Floor: {self.floor}, Type: {self.type}, Area: {self.area}"
