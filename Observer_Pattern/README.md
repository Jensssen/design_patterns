# Observer Pattern

## Version 1
Let us assume we have a Weather station, represented by an object and this object is constantly changing due to changing weather conditions. 
Now let us assume that we have a second object that wants to subscribe to the weather station object. It wants to keep track on every change of the
weather station object. This is where the observer patter comes into play. 

The idea behind the observer pattern is that the observed object pushes its changes to all objects that are "subscribing" to it. 
The reason why we push information instead of pulling it by the different objects is that this is much more resource efficient. 

The weather station object is called observable and the subscribing objects are called observers.  

TLDR;
-   The observer pattern defines a one to manny relationship/dependency between objects so that when one object changes its state (only the observable one, not any) all of its dependend objects get notified and updated automatically.

## Version 2
`version2.py` also implements the observer pattern. However, it applies a slightly different example. Version one is a bit similar to an IoT use case.
Version 2 is a bit closer to a User management system. Here we have a User Management class that can register and delete users of the app. 
The User Management class also has access to a preconfigured notification service object that holds a list/dict of subscribed services. One is a log service
and the other one is a mail service. By preconfiguring the notification service class (adding the log service and the email service as subscribers), we can not call
the `notify` method after adding or deleting a user. If the passed event type is present, the corresponding log and email actions are triggered. 

In other words, the log service and the email service are observing the user management class. If the user management class adds or deletes a new user, corresponding 
events are being triggered which are decoupled from the user management class via the common notification service. 