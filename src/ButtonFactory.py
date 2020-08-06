from telegram import ReplyKeyboardMarkup, KeyboardButton
from src.utils.utils import MenuLevel


class ButtonFactory:
    default_menu_buttons = {MenuLevel.BASKET: 'Basket', MenuLevel.ORDER: 'Order', MenuLevel.BACK: 'Back'}
    default_menu_responses = {MenuLevel.MAIN: "Choose Category:", MenuLevel.ITEMS: "Choose Items:",
                              MenuLevel.QUANTITY: "Choose Quantity:"}
    #TODO Add all menu responses
    @staticmethod
    def get_main_menu_buttons():
        keyboard = ButtonFactory.generate_categories_buttons()
        keyboard.append([KeyboardButton("Basket"), KeyboardButton("Order")])
        return keyboard

    @staticmethod
    def in_menu_default_buttons():
        return [["Back"], ["Basket", "Order"]]

    @staticmethod
    def generate_categories_buttons():
        return []

    @staticmethod
    def generate_quantity_buttons():
        # TODO:
        # get_quantity -> function item quantitiy get as limit and create keyboards in list or an array
        keyboard = [[KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3")],
                    [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6")],
                    [KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9")]]
        return keyboard
