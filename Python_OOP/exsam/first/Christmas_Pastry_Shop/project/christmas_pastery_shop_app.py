from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShpApp:

    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    VALID_BOOTHS = {
        "Open Booth":OpenBooth,
        "Private Booth":PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):
        delicacy = [d for d in self.delicacies if d.name == name]

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name,price)
        self.delicacies.append(delicacy)

        return  f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        booth = [b for b in self.booths if b.booth_number == booth_number]

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and b.is_reserved ,self.booths))

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            both = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception (f"No {delicacy_name} in the pastry shop!")

        both.delicacy_orders.apend(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        both = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        bill = both.price_for_reservation + sum(d.price for d in both.delicacy_orders)

        both.delicacy_orders.clear()
        both.is_reserved = False
        both.price_for_reservation = 0

        self.income += bill
        return f"Booth {booth_number}:\n"\
                f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



