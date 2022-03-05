class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_lenght_password = len(value) >= 8
        is_upper_password = any([True for x in value if x.upper()])
        is_digit_password = any([True for x in value if x.isdigit()])

        if is_lenght_password and is_upper_password and is_digit_password:
            self.__password = value
            return
        raise ValueError ('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
