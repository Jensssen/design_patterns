from Beverage import Beverage


class Decorator(Beverage):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _beverage: Beverage = None

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @property
    def beverage(self) -> int:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._beverage

    def get_cost(self) -> int:
        return self._beverage.get_cost()
