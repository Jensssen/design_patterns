# Observer Pattern

Lets assume we have a Weather station, represented by an object and this object is constantly changing due to changing weather conditions. 
Now lets assume that we have a second object that wants to subscribe to the weather station object. It wants to keep track on every change of the
weather station object. This is where the observer patter comes into play. 

The idea behind the observer pattern is that the observed object pushes its changes to all objects that are "subscribing" to it. 
The reason why we push information instead of pulling it by the different objects is that this is much more resource efficient. 

The weather station object is called observable and the subscribing objects are called observers.  

TLDR;
-   The observer pattern defines a one to manny relationship/dependency between objects so that when one object changes its state (only the observable one, not any) all of its dependend objects get notified and updated automatically. 