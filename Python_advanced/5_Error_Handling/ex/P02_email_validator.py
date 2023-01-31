from _ast import pattern


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

MIN_LENGTH = 4


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != "End":

    if len(email.split("@")[0]) <= MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
