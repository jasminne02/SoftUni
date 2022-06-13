class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == 'End':
        break

    email = command.split('@')

    if len(email) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters.")

    domain = domain.split('.')
    domain = domain[-1]

    if domain not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
