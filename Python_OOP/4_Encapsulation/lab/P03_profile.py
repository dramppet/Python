class Profile:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password


    @property
    def username(self):
        return self.__username


    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,value:str):
        if len(value) < 8 or not any(s.isdigit() for s in value ) or not any(s.isalpha()  and s == s.upper() for s in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {len(self.__password) * "*"}'


profile_with_invalid_password = Profile('My_username', 'My-password')