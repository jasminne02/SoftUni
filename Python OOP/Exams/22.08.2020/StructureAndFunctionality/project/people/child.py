class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = self.__sum_cost(food_cost, *toys_cost)

    @staticmethod
    def __sum_cost(food_cost: int, *toys_cost):
        cost = food_cost
        for toy in toys_cost:
            cost += toy
        return cost
