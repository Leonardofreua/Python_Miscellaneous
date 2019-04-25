Design Patterns: Python
=======================

A collection containing the catalog of Design Patterns, some Sorting Algorithms, Thread Life Cycle and other small Algorithms. Below you will see the lists with the protagonists of this collections. 

## **Design Patterns**:

**Behavioral Patterns**:

| Pattern | Description |
|:-------:| ----------- |
| [Chain of Responsibility](Behavioral/ChainOfResponsability.py) | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it. |
| [Command](Behavioral/Command.py) | Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations.	 |
| [Observer or Publish/Subscribe](Behavioral/PublishSubscribe/DriverObserver.py) | Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.	 |
| [Observer](Behavioral/State.py) | called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.	 |
| [State](Behavioral/State.py) | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.	 |
| [Strategy](Behavioral/Strategy.py) | Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.	 |
| [Template](Behavioral/Template.py) | Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.	 |
| [Visitor](Behavioral/Visitor.py) | Represent an operation to be performed on the elements of an object structure. Visitor lets a new operation be defined without changing the classes of the elements on which it operates.		 |


**Creational Patterns**:

| Pattern | Description |
|:-------:| ----------- |
| [Abstract Factory](Creational/AbstractFactory.py) | Provide an interface for creating families of related or dependent objects without specifying their concrete classes.	|
| [Builder](Creational/Builder.py) | Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.	 |
| [Factory](Creational/Factory.py) | Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.		 |
| [Prototype](Creational/Prototype.py) | Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum.		 |
| [Singleton](Creational/Singleton.py) | Ensure a class has only one instance, and provide a global point of access to it.		 |



**Structural Patterns**:

| Pattern | Description |
|:-------:| ----------- |
| [Adapter](Structural/Adapter.py) | Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator.		|
| [Decorator](Structural/Decorator.py) | Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.		 |
| [Facade](Structural/Facade.py) | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.			 |
| [Proxy](Structural/Proxy.py) | Provide a surrogate or placeholder for another object to control access to it.			 |
| [MVC](Structural/MVC/main.py) | MVC Pattern stands for [Model](Structural/MVC/Model.py)-[View](Structural/MVC/View.py)-[Controller](Structural/MVC/Controller.py) Pattern. This pattern is used to separate application's concerns.