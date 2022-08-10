from project.bakery import Bakery

bakery = Bakery('MyBakery')
print(bakery.add_table('OutsideTable', 53, 4))
print(bakery.add_table('OutsideTable', 57, 7))
print(bakery.add_table('OutsideTable', 56, 9))
print(bakery.add_food('Cake', 'chocolate cake', 3.42))
print(bakery.add_food('Bread', 'bread', 1))
print(bakery.reserve_table(4))
print(bakery.order_food(53, 'cake', 'bread', 'chocolate cake'))
print(bakery.leave_table(53))
print(bakery.get_total_income())
print(bakery.get_free_tables_info())
