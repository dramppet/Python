from typing import List

from project.band import Band
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert

from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def musician_name(self):
        return [m.name for m in self.musicians]

    @property
    def bands_name(self):
        return [b.name for b in self.bands]

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")

        musician_name = self.musician_name

        if name in self.musician_name:
            raise Exception(f"{name} is already a musician!")

        m = None
        if musician_type == "Guitarist":
            m = Guitarist(name, age)
        elif musician_type == "Drummer":
            m = Drummer(name, age)
        elif musician_type == "Singer":
            m = Singer(name,age)

        self.musicians.append(m)

        return f"{name} is now a {musician_type}."
    def create_band(self, name: str):
        band = self.bands_name

        if name in band:
            raise Exception (f"{name} band is already created!")

        b = Band(name)
        self.bands.append(b)

        return f"{name} was created."
    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]

        if concert:
            raise Exception(f"{place} is already registered for {genre} concert!")

        c = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(c)
        return f"{genre} concert in {place} was added."
    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self.musician_name:
            raise Exception (f"{musician_name} isn't a musician!")

        if band_name not in self.bands_name:
            raise  Exception(f"{band_name} isn't a band!")
        mus_ex = [ m for m in self.musicians if m.name == musician_name][0]
        band_ex = [ b for b in self.bands if b.name == band_name][0]

        band_ex.members.append(mus_ex)

        f"{musician_name} was added to {band_name}."
    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.bands_name:
            raise Exception(f"{band_name} isn't a band!")
        if musician_name not in self.musician_name:
            raise Exception(f"{musician_name} isn't a musician!")

        band_ex = [ b for b in self.bands if b.name == band_name][0]
        mus_in_band = [m for m in band_ex.members if m.name == musician_name]

        musician = mus_in_band[0]
        band_ex.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        musician_type = set([m.__class__.__name__ for m in self.band.members])

        if musician_type < 3:
            raise Exception (f"{band_name} can't start the concert because it doesn't have enough members!")

        singers = [s for s in band.members if isinstance(s, Singer)]
        drummers = [s for s in band.members if isinstance(s, Drummer)]
        guitarist = [s for s in band.members if isinstance(s, Guitarist)]

        are_singers = True
        for singer in singers:
             if concert.genre == "Rock":
                  if "sing high pitch notes" not in singer.skills:
                        are_singers = False
             elif concert.genre == "Metal":
                  if "sing low pitch notes" not in singer.skills:
                      are_singers = False
             elif concert.genre == "Jazz":
                 if "sing high pitch notes and sing low pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                     are_singers = False

        are_drummers = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "lay the drums with drumsticks" not in drummer.skills:
                    are_drummers = False
            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers = False
            elif concert.genre == "Jazz":
                if "ay the drums with drum brushes" not in drummer.skills:
                    are_drummers = False

        are_guitarist = True
        for guitarist in guitarist:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarist = False
            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    are_guitarist = False
            elif concert.genre == "Jazz":
                if "aplay jazz" not in guitarist.skills:
                  are_guitarist = False

        if not are_guitarist or not  are_drummers or not are_singers:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
