def shopping_cart(*args):
    meal_dict = dict()

    for info in args:
        if "Stop" in info:
            break

        meal_type, product = info

        if meal_type not in meal_dict:
            meal_dict[meal_type] = []
            meal_dict[meal_type].append(product)
        elif meal_type == "Soup" and len(meal_dict[meal_type]) < 3:
            if product not in meal_dict[meal_type]:
                meal_dict[meal_type].append(product)
        elif meal_type == "Pizza" and len(meal_dict[meal_type]) < 4:
            if product not in meal_dict[meal_type]:
                meal_dict[meal_type].append(product)
        elif meal_type == "Dessert" and len(meal_dict[meal_type]) < 2:
            if product not in meal_dict[meal_type]:
                meal_dict[meal_type].append(product)

    if len(meal_dict) == 0:
        return "No products in the cart!"

    if "Pizza" not in meal_dict:
        meal_dict["Pizza"] = []
    if "Soup" not in meal_dict:
        meal_dict["Soup"] = []
    if "Dessert" not in meal_dict:
        meal_dict["Dessert"] = []

    meal_dict = sorted(
        meal_dict.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    sorted_meals = dict()
    meals_string = ""

    for meal, products in meal_dict:
        products = sorted(products)
        sorted_meals[meal] = products

    for meal, products in sorted_meals.items():
        meals_string += meal + ":\n"
        for product in products:
            meals_string += " - " + product + "\n"

    return meals_string


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
