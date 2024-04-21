# Visitor Pattern

## Version 1
In `version1.py` we have two products (Milk and Alcohol) which both implement two buy methods from a shared abstract class called Product. 
One buy method applies a taxation and the other one does not. 
This Implementation looks nice at the first glance. However, what if we want to implement country specific taxation methods. 
This would require us to go into every single `buy_product_without_tax` method, and adjust it. This would not only violate the 
single responsibility and open-close principle, it would also make the entire code even more difficult to maintain. See `version1_1.py`. 

## Version 1.1
In `version1_1.py` we have added a German and a French specific taxation to our products. For that we had to add a country code dependent if block in each product class. 
It is obvious that this does not scale, is hard to maintain and will highly decrease cohesion. 

## Version 2 (Visitor Pattern)
The visitor pattern allows us to extract and separate a common behaviour or algorithm from an object on which they operate. 
This can be achieved by creating an often called abstract `Visitor` class and move the common behaviour into subclasses of that Visitor class.
In our example we create a `GermanTaxation` and a `FrenchTaxation` subclass. Each implement a country specific
taxation algorithm for milk and alcohol. 
Finally, we make use of the country specific taxation methods by applying a technique called `Double Dispatch`. 
Each `buy_produt_including_tax` method now takes as an input argument a specific visitor (tax method) implementation and calls the
appropriate product taxation method. 
This approach allows us to isolate the taxation behaviour from product objects on which they operate and place them into a single class.
The product classes will be more focused on their main job, hence following the Single Responsibility principle. 
Also, new visiting behaviors can be easily introduced without modifying existing ones, following the Open-Closed Principle. 
Finally, visitors (Taxation methods in this case) are easily interchangeable by clients at runtime. 
