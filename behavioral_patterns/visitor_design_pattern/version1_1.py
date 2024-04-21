from __future__ import annotations

from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, price_before_tax: float):
        self.price_before_tax = price_before_tax

    @abstractmethod
    def buy_product_without_tax(self) -> float:
        pass

    @abstractmethod
    def buy_product_including_tax(self, country: str) -> float:
        pass


class Milk(Product):
    def __init__(self, price_before_tax: float):
        super().__init__(price_before_tax)

    def buy_product_including_tax(self, country_code: str) -> float:
        if country_code == "GER":
            product_price = self.price_before_tax + self.price_before_tax * 0.07
        elif country_code == "FR":
            product_price = self.price_before_tax + self.price_before_tax * 0.10
        else:
            raise KeyError(f"Country code {country_code} not supported.")
        print(f"Product bought, including tax for {product_price}")
        return product_price

    def buy_product_without_tax(self) -> float:
        product_price = self.price_before_tax
        print(f"Product bought, without tax for {product_price}")
        return product_price


class Alcohol(Product):
    def __init__(self, price_before_tax: float):
        super().__init__(price_before_tax)

    def buy_product_including_tax(self, country_code: str) -> float:
        if country_code == "GER":
            product_price = self.price_before_tax + self.price_before_tax * 0.19
        elif country_code == "FR":
            product_price = self.price_before_tax + self.price_before_tax * 0.20
        else:
            raise KeyError(f"Country code {country_code} not supported.")
        print(f"Product bought, including tax for {product_price}")
        return product_price

    def buy_product_without_tax(self) -> float:
        product_price = self.price_before_tax
        print(f"Product bought, without tax for {product_price}")
        return product_price


if __name__ == '__main__':
    milk = Milk(1)
    milk.buy_product_without_tax()
    milk.buy_product_including_tax("GER")
    print("\n")
    milk = Milk(1)
    milk.buy_product_without_tax()
    milk.buy_product_including_tax("FR")

    alc = Alcohol(12)
    alc.buy_product_without_tax()
    alc.buy_product_including_tax("GER")
    print("\n")
    alc = Alcohol(12)
    alc.buy_product_without_tax()
    alc.buy_product_including_tax("FR")