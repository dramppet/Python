class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

MIN_LENGTH = 4
valid_domains = [".com", ".bg", ".net", ".org"]

pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != "End":

    if len(email.split("@")[0]) <= MIN_LENGTH:
        raise NameTooShortError(f"Name must be more than {MIN_LENGTH} characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if findall(pattern_domain, valid_domains)[-1]:
        raise InvalidDomainError (f"Domain must be one of the following: {', '.join(valid_domains)}")

