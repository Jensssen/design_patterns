from Decorator import Decorator


class SoyDecorator(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def get_cost(self) -> int:
        print("You added Soy of cost 1")

        return self.beverage.get_cost() + 1
