from Decorator import Decorator


class CaramelDecorator(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def get_cost(self) -> int:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """

        print("You added Caramel of cost 2")
        return self.beverage.get_cost() + 2
