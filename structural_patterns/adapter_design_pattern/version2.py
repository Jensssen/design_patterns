from abc import ABC, abstractmethod
from typing import Dict, List


class FancyApp(ABC):

    @abstractmethod
    def display_products(self, products: Dict[str, List[str]]) -> None:
        pass


class OldApp(FancyApp):

    def display_products(self, products: Dict[str, List[str]]) -> None:
        for idx, product in enumerate(products["products"]):
            print(f"{idx + 1}: Product: {product}")


class NewApp(FancyApp):

    def display_products(self, products: Dict[str, List[str]]) -> None:
        for idx, product in enumerate(products["items"]):
            print(f"{idx + 1}: Product: {product}")


class NewAppAdapter(FancyApp):

    def display_products(self, products: Dict[str, List[str]]) -> None:
        new_app = NewApp()

        adapted_data = {"items": products["products"]}

        new_app.display_products(adapted_data)


if __name__ == '__main__':
    old_app = OldApp()
    print("Old app:")
    old_app.display_products({"products": ["Book", "Car", "Pullover"]})
    print("\n")
    new_app = NewApp()
    print("New app:")
    # New App only works with the key being items.
    new_app.display_products({"items": ["Book", "Car", "Pullover"]})
    print("\n")
    new_app_adapter = NewAppAdapter()
    print("New app using its adapter:")
    # Using the custom new app adapter, we can still pass a dict that uses products as key.
    new_app_adapter.display_products({"products": ["Book", "Car", "Pullover"]})
