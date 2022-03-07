# class CreditCard:
#     def __init__(self, number, ep_date, cvv, pin ):
#         self.number = number
#         self.ep_date = ep_date
#         self.cvv = cvv
#         self.__pin = pin
#         a = 5
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#         raise ValueError('Please again pin')
#
#
# c = CreditCard(12389654526, '2022-10', 123456789, 1234)
# print(c.number)
# print(c._CreditCard__pin)
#
# c.change_pin(1234, 6789)
#
# print(c._CreditCard__pin)
# c.change_pin(8523,0000)

class Person:
    def __init__(self, age):
        self.age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 18:
            self.__age = 18
        self.__age = value

p = Person(5)
p.age = 6
print(p.age)