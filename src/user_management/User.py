from collections import deque
class User:

    def __init__(self, id):
        self.id = id
        self.menu = deque()
        self.curr_menu_level = 0
        self.curr_category = None
        self.curr_food = None
        self.basket = dict()
        self.total_cost = 0

    def get_curr_menu_level(self):
        if len(self.menu) > 0:
            return self.menu[len(self.menu) - 1]
        else:
            return 0

    def set_curr_menu_level(self, level):
        self.menu.append(level)

    def get_id(self):
        return self.id

    @staticmethod
    def add_to_db():
        pass
