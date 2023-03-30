from project.booths.booth import Booth


class OpenBooth(Booth):
    @ property
    def get_price_per_person(self):
          return 2.50
    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * self.price_for_reservation
        self.is_reserved = True