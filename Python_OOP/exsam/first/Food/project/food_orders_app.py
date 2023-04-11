from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):

        if self.__check_if_client_exists(client_phone_number):
            raise Exception("The client has already been registered!")

        current_client = Client(client_phone_number)
        self.clients_list.append(current_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self.__check_menu()

        details_meals_in_menu = []

        for meal in self.menu:
            details_meals_in_menu.append(meal.details())

        return "\n".join(details_meals_in_menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_menu()

        if not self.__check_if_client_exists(client_phone_number):
            self.register_client(client_phone_number)

        current_client: object
        self.__find_client(client_phone_number)

        current_client = self.__find_client(client_phone_number)

        current_shopping_card = []
        current_bill = 0.0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if not self.__check_if_meal_is_is_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = self.__find_meal(meal_name)

            if current_meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {type(current_meal).__name__}: {current_meal.name}!")


        for meal_name, meal_quantity in meal_names_and_quantities.items():
            current_meal = self.__find_meal(meal_name)
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_quantity
            current_meal.quantity -= meal_quantity




    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __check_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __check_if_client_exists(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return True

    def __find_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def __check_if_meal_is_is_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return True

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
