from __future__ import annotations

from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, price_before_tax: float):
        self.price_before_tax = price_before_tax

    @abstractmethod
    def buy_product_without_tax(self) -> float:
        pass

    @abstractmethod
    def buy_product_including_tax(self, product_specific_tax_method: Visitor) -> float:
        pass


class Milk(Product):
    def __init__(self, price_before_tax: float):
        super().__init__(price_before_tax)

    def buy_product_including_tax(self, product_specific_tax_method: Visitor) -> float:
        product_price = self.price_before_tax + product_specific_tax_method.for_milk(self)
        print(f"Product bought, including tax for {product_price}")
        return product_price

    def buy_product_without_tax(self) -> float:
        product_price = self.price_before_tax
        print(f"Product bought, without tax for {product_price}")
        return product_price


class Alcohol(Product):
    def __init__(self, price_before_tax: float):
        super().__init__(price_before_tax)

    def buy_product_including_tax(self, product_specific_tax_method: Visitor) -> float:
        product_price = self.price_before_tax + product_specific_tax_method.for_alcohol(self)
        print(f"Product bought, including tax for {product_price}")
        return product_price

    def buy_product_without_tax(self) -> float:
        product_price = self.price_before_tax
        print(f"Product bought, without tax for {product_price}")
        return product_price


class Visitor(ABC):
    @abstractmethod
    def for_milk(self, product: Milk) -> float:
        pass

    @abstractmethod
    def for_alcohol(self, product: Alcohol) -> float:
        pass


class GermanTaxation(Visitor):

    def for_milk(self, product: Milk) -> float:
        print("Apply German Taxation.")

        return product.price_before_tax * 0.07

    def for_alcohol(self, product: Alcohol) -> float:
        print("Apply German Taxation.")
        return product.price_before_tax * 0.19


class FrenchTaxation(Visitor):

    def for_milk(self, product: Milk) -> float:
        print("Apply French Taxation.")
        return product.price_before_tax * 0.1

    def for_alcohol(self, product: Alcohol) -> float:
        print("Apply French Taxation.")
        return product.price_before_tax * 0.2


if __name__ == '__main__':
    milk = Milk(1)
    milk.buy_product_without_tax()
    milk.buy_product_including_tax(GermanTaxation())
    milk = Milk(1)
    milk.buy_product_without_tax()
    milk.buy_product_including_tax(FrenchTaxation())
    print("\n")
    alc = Alcohol(12)
    alc.buy_product_without_tax()
    alc.buy_product_including_tax(GermanTaxation())
    alc = Alcohol(12)
    alc.buy_product_without_tax()
    alc.buy_product_including_tax(FrenchTaxation())
