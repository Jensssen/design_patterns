from Soy_Decorator import SoyDecorator
from Caramel_Decorator import CaramelDecorator
from Decaf import Decaf
from Espresso import Espresso
from Beverage import Beverage


def get_total_cost_of_order(beverage: Beverage) -> None:
    print(f"Your Ordered Beverage costs: {beverage.get_cost()}")


if __name__ == "__main__":
    espresso = Espresso()
    get_total_cost_of_order(espresso)
    print("\n")

    soy_decorator = SoyDecorator(espresso)
    caramel_decorator = CaramelDecorator(soy_decorator)

    get_total_cost_of_order(caramel_decorator)
