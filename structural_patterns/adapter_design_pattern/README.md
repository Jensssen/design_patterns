# Adapter Pattern

## Version 1
In `version1.py` the adapter patter is a structural pattern, and it is used to connect two different "interfaces" (Target and Adaptee). 
It converts the interface of the Adaptee class so that it is the same as the Target interface, using an Adapter class in between.
An adapter lets classes work together that could not otherwise because of incompatibility. Version 2 
shows a second example of the Adapter Pattern. 

## Version 2

In `version2.py` we can see an abstract class called FancyApp which is implemented by two subclasses (OldApp and NewApp).
Both apps implement a display_product method which prints out a list of products, passed via a Dictionary. 
Unfortunately, the new app expects the key of the product dictionary to be "items" and the old app expects the key to be "products". 
A client that is calling the display method of the old app and the new up has to take this into account and provide a compatible Dictionary. 

The different "contracts" of the old and new app can be aligned by implementing an Adapter, particularly for the New App. 
It implements the same `display_products` method which calls the `display_product` method of the New App. 
However, before doing that, it adapts or adjusts the Dictionary key, changing it from "product" to "items", so that the New App
can process the initial dictionary just like the Old App. 