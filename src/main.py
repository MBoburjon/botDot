# an initial comment before starting the project
# A bot for telegram

import logging
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
from src.user_management import User
from src.ButtonFactory import ButtonFactory
from src.utils import utils
from src.utils.utils import MenuLevel
from enum import IntEnum


class Bot:

    def __init__(self, token):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.users = list()

        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        update_handler = MessageHandler(Filters.text & (~Filters.command), self.update_func)
        self.dispatcher.add_handler(update_handler)
        self.categories = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9']
        self.items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8']

    def start(self, update, context):
        curr_user = self.get_curr_user(update)
        keyboard = self.get_keyboard(curr_user)
        print(keyboard)
        rply_markup = ReplyKeyboardMarkup(keyboard)
        rply_markup.resize_keyboard = True
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hamma harajatlarni aytaverasiz. Aka hizmatdamiz!!!", reply_markup=rply_markup)

    def update_func(self, update, context):
        curr_user = self.get_curr_user(update)
        update_text = update.effective_message.text
        print("is1")
        print(update.effective_chat.id, ":", update.effective_message.text)
        if update_text == ButtonFactory.default_menu_buttons[MenuLevel.BACK]:
            curr_user.menu.pop()
            print("poped menu level")

        if update_text in self.categories:
            curr_user.menu.append(MenuLevel.ITEMS)
            curr_user.curr_category = update_text
            reply_text = "Choose Item:"

        if update_text in self.items:
            curr_user.menu.append(MenuLevel.QUANTITY)
            curr_user.curr_food = update_text
            reply_text = "Choose Quantity:"

        if update_text == ButtonFactory.default_menu_buttons[MenuLevel.BASKET]:
            curr_user.menu.append(MenuLevel.BASKET)

        reply_text = ButtonFactory.default_menu_responses[curr_user.get_curr_menu_level()]
        keyboard = self.get_keyboard(curr_user)
        reply_markup = ReplyKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text, reply_markup=reply_markup)

    def get_curr_user(self, update):
        current_user = None
        if any(user.id != update.effective_chat.id for user in self.users) or len(self.users) == 0:
            current_user = User(update.effective_chat.id)
            current_user.add_to_db()
            self.users.append(current_user)
            print(current_user)

        else:
            for user in self.users:
                if user.id == update.effective_chat.id:
                    current_user = user
        return current_user

    def get_keyboard(self, user: User):
        categories = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9']
        items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8']
        keyboards = {}
        main = utils.to_nx2_matrix(categories)
        main.append(*ButtonFactory.get_main_menu_buttons())
        keyboards[MenuLevel.MAIN] = main

        items_k = utils.to_nx2_matrix(items)
        for i in ButtonFactory.in_menu_default_buttons():
            items_k.append(i)
        keyboards[MenuLevel.ITEMS] = items_k
        keyboards[MenuLevel.QUANTITY] = ButtonFactory.generate_quantity_buttons()
        keyboards[MenuLevel.QUANTITY].extend(ButtonFactory.in_menu_default_buttons())

        #TODO finish all keyboards
        print(keyboards[user.get_curr_menu_level()])
        return keyboards[user.get_curr_menu_level()]


if __name__ == '__main__':

    #bot = Bot('1221385179:AAFQHv8RcaYmJ1R61gi-rNWP2681KChxv34')
    bot = Bot('1349984757:AAE8BcUnXvWDsiQ-GdjbRmnAptUhdy7tyL4')
    bot.updater.start_polling()
