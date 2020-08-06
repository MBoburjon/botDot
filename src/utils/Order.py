#Order class and files control
class Orders:
    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity

    # order_id getter function
    @property
    def orid_func(self):
        return self.order_id

    # order_id setter function override
    @orid_func.setter
    def orid_func(self, order_id):
        self.order_id = order_id

    # item_id getter function
    @property
    def item_id_func(self):
        return  self.item_id

    # item_id setter function
    @item_id_func.setter
    def item_id_func(self, item_id):
        self.item_id = item_id

    # quantity getter function
    @property
    def quantity_func(self):
        return self.quantity

    # quantity setter function
    @quantity_func.setter
    def quantity_func(self, quantity):
        self.quantity = quantity