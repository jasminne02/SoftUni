import re


class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, email):
        regex = r"([a-z0-9\_\.]+)\@([a-z]+)\.([a-z]+)"
        matches = re.search(regex, email)
        name = matches.group(1)
        mail = matches.group(2)
        domain = matches.group(3)

        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False

    def __is_name_valid(self, name):
        if len(name) >= self.__min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.__mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.__domains:
            return True
        return False

    @property
    def min_length(self):
        return self.__min_length

    @min_length.setter
    def min_length(self, value):
        if value > 0:
            self.__min_length = value

    @property
    def mails(self):
        return self.__mails

    @mails.setter
    def mails(self, value):
        if len(value) > 0:
            self.__mails = value

    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, value):
        if len(value) > 0:
            self.__domains = value


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
