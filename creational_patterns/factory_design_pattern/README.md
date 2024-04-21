# Factory Pattern / Abstract Factory Pattern

## Version 1

In `version1.py` we have a car class that is created by a `create_vehicle` function. Inside the main function, different
car class methods are called.
For now, there are no big issues with this code, mainly because it is very minimal.
In Version 2 we are adding a second class and some custom logic to this which will indicate first small issues with this
code.

## Version 2

In `version2.py` we have added a truck class next to the car class. The `create_vehicle` function also got some custom
logic
which instantiates and returns either a car or a truck object, depending on the requested vehicle type (fast or slow).
The introduction of a second class indicates some small issues in our code. The logic in `create_vehicle` must change
every time, we add new vehicles.
Also, if Car and Truck do not implement the same methods, we will get an error in our main function. Especially the
second problem will be addressed in Version 3.

## Version 3 (Simple Factory Idiom)

In `version3.py` we have added an abstract Vehicle class that Car and Truck must implement. This fixes the issue of not
implementing certain methods which might be called later on in main.
The implemented structure in Version 3 is also called the "Simple Factory Idiom". It is not the factory design pattern
yet.
What is nice about it is that it already follows
the [single responsibility](https://en.wikipedia.org/wiki/Single_responsibility_principle) principles.
However, if we add more types of vehicles, we will need to _open_ the create_vehicle method (add more if statements)
which violates the  [open-closed](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle) principle.
Version 4 illustrates this by adding more vehicles.

## Version 3.1

In `version3_1.py` we added additional vehicle classes (Airplane and Helicopter) which results into some necessary
changes inside the `create_vehicle` method.
This violates the [open-closed](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle) principle, because we have
to go into the `create_vehicle` method and change it's if logic when ever we add new classes.

## Version 4 (Factory Design Pattern)

In `version4.py` we remove the Airplane and Helicopter class for now. However, a big change with respect
to `version3.py` is that we introduce an abstract VehicleFactory class and two subclasses (FastGroundVehicleFactory and
SlowGroundVehicleFactory).
The abstract VehicleFactory class has an abstract method called create_vehicle that all subclasses must implement.
**This method is in fact the factory method**. It delegates the object creation to subclasses. The business logic is not part of the
VehicleFactory anymore, since the user of the Factory can now instantiate the concrete VehicleFactory subclass they need
and the correct Vehicle object will be returned to the user. The user has full control over the business logic now and
the [open-closed](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle) principle is not violated anymore because
the user can simply add more vehicle classes without touching the VehicleFactory. Keep in mind that we could have kept
the
if else logic inside the VehicleFactory which would violate the open-close principle. In that case we would still follow
the Factory Method pattern, so just applying the pattern does not automatically lead to the fulfillment of such
principles. It is just a pattern that provides a structure to improve the extendability and maintainability of our
overall solution , but it still requires the developer to be aware of [SOLID](https://en.wikipedia.org/wiki/SOLID)
principles.

## Version 5 (Abstract Factory Design Pattern)

In `version5.py` we again added the Airplane and Helicopter Class which both inherit from an AirVehicle class.
The Car and the Truck inherit from a GroundVehicle Class as well.
Now let's assume that our business logic has to change in a way that we want to either use only air vehicles or only
ground vehicles (maybe depending on the distance that we have to deliver goods or if we have to cross mountains or
oceans...). In this case, it is recommended to apply the Abstract Factory Design Pattern. We can achieve this by having 
two factory methods in our VehicleFactory class. One for Ground Vehicles and one for Air Vehicles. 
Then we create two sub-class-factories which implement those factory methods, one for ground and one for air vehicles.
Now we can change our business logic accordingly. **The Abstract Factory Design Pattern again separates the creation of 
objects from its use (high Cohesion) and it helps to group objects that belong together.** 
