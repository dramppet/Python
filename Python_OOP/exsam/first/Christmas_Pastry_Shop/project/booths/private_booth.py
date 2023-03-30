from project.booths.booth import Booth


class PrivateBooth(Booth):

    @property
    def get_price_or_one_person(self):
        return 3.50

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * self.price_for_reservation
        self.is_reserved = True