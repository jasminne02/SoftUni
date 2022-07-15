from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscription = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscription:
            self.subscription.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""
        customer_id = None
        trainer_id = None
        exercise_plan_id = None
        exercise_plan = None
        equipment_id = None

        for subscription in self.subscription:
            if subscription.id == subscription_id:
                result += subscription.__repr__() + "\n"
                customer_id = subscription.customer_id
                trainer_id = subscription.trainer_id
                exercise_plan_id = subscription.exercise_id

        for customer in self.customers:
            if customer_id == customer.id:
                result += customer.__repr__() + "\n"
        for trainer in self.trainers:
            if trainer_id == trainer.id:
                result += trainer.__repr__() + "\n"

        for plan in self.plans:
            if plan.id == exercise_plan_id:
                equipment_id = plan.equipment_id
                exercise_plan = plan

        for equipment in self.equipment:
            if equipment.id == equipment_id:
                result += equipment.__repr__() + "\n"

        result += exercise_plan.__repr__()
        return result
