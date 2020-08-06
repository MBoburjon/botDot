# create table order_list(
# 	user_id	varchar(20),
# 	order_id varchar(20) PRIMARY KEY,
# 	order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# 	location varchar(30),
# 	contact_number varchar(20));
#
# # Creating order table
# create table ordered_items_list(
# 	item_id varchar(20),
# 	order_id varchar(20),
# 	quantity varchar(20));s

import src.utils.Order

class order_control:

    @staticmethod
    def add_order():
        pass
