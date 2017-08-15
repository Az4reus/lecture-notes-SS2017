# Overview, EIST #5
At the end of this lecture I should be able to

- Understand the difference between coupling and cohesion
- Understand the eight most important issues in system design
- Understand the implementation of the facade and proxy patterns. 

# Content
A *Facade* is basically an API, but not yet programmed, only designed. Only the
implementation is called an API, not the designed path. 

## Cohesion and Coupling

- *Cohesion* maeasures the interdependence of objects in *one* subsystem
- *Coupling* measures the interdependence of objects between *different*
  subsystems.

###Achieving High Cohesion/Low Coupling: 

*High Cohesion:* 

- Operations work on same attributes
- Operations implement a common abstraction or service

*Low Coupling:* 

- Small interfaces
- Information hiding
- No global state
- Interactions mostly within subsystem rather than across boundaries.

### Cohesion and Model Transformation definitions

- Model transformation (Model refactoring) = Changing a model to be better
- "Forward engineering" = Translating model to code. More generally, this
  describes translating any model. *(cf. reverse engineering, going from code
  to model)*
- Refactoring = refactoring (This time in code)

## Elements of an Architectural Style

- *Components (Subsystems)*: Computational units with a specified interface.
  (e.g. filters, databases, layers, objects)
- *Connectors (Communication)*: Interactions between components (e.g. method
  calls, pipes, events, shared data.)

### Layered Architecture in terms of Componens & Connectors

- Subsystems: Group of subtasks which implement an abstraction at some layer in
  the hierarchy
- Protocols that define how the layers interact.

### Facade Pattern

- A facade provides a unified interface for a subsystem. 
    - A facade consists of a set of public operations
    - Each public operation is delegated to one or more operations in the
      classes behind the facade. 
- A facade defines a higher-level interface that makes the subsystem easier to
  use (it abstracts out the gory details and the spaghettit)

### MVC In terms of C&C

- Components: 
    - *Model*: contains core functionality and data
    - *View*: Displays information to the user in some form
    - *Controller*: handles user input.
- Connectors: 
    - Events: Change-propagation mechanism via events ensures consistency
      between user interface and model
    - Method calls:
        - Stuff like `readData()`, etc. 
        - If the user changes the model through the controller of one view, the
          other views will be updated automatically.

## Concurrency

- Used to address nonfunctional requirements such as: Performance, Response
  Time, latency, availability.
- Two objects are *inherently concurrent* if they can receive events at the
  same time without interacting.
      - Identification: Objects in a sequence diagram that are independent. 
- Inherently concurrent objects can be assigned to separate threads of
  control. 

### Thread of control 
A *Thread of Control* is a path through a set of state diagrams where only a
single object is active at any time.

*Thread Splitting*: Object sends non-blocking event to another object, so it
doesn't block.

Concurrent Threads leads to *race conditions.* This is a design flaw where the
output of a process depends on the specific sequence of other events.

### Concurrency Questions

- To identify threads for concurrency we ask the following questions: 
    - Deos the system provide access to multiple users?
    - Which entity objects of the object model can be executed independently
      from each other? 
    - What kinds of control objects are identifiable? 
    - Can a single request be decomposed into mltiple requests? 

### Implementing Concurrency.

Concurrent systems can be implemented on any system that provides 
concurrency. Two types:  

- *Physical Concurrency:* Threads are provided by hardware. (Multiprocessors,
  RPC, etc) 
- *Logical Concurrency*: Threads provided by software (pthreads, thread packages)

## Hardware/Software Mapping

This System Design activity addresses two questions: 

1. How do we realise the subsystems? Hardware or software? 
2. How do we map the object madel from analysis to hardware and/or software? 

### H/S Mapping difficulties

Much of the difficulty of designing a system comes from addressing
externally-imposed hardware and software constraints. 

### Two new UML Diagram Types

- *Component Diagram:* Illustrates dependencies between components at design
  time, compilation time and runtime
      - Dependencies are described as *dashed lines* with arrows.
      - Provided and required interfaces are described with Lollipop/Socket
        notation
- *Deployment Diagram*: Illustrates the distribution of components on concurrent
  processes at runtime
      - Useful after decomposition, concurrency and H/S Mapping already
        happened.
      - Nodes are shown as 3-D boxes. 
      - Connections are shown as solid lines.
      - Nodes may contain components. (Hybrid between Component and Deployment
        diagram.)

### Middleware

Middleware is _glue_, that provides useful and easy-to-use abstractions. The
whole TCP/IP stack abstracts into Sockets, the physical connection between
computers abstracts into a wire and a device. 

## Persistent Data Management

- All classes of type `<<entity>>` in the system model need to be persistent: 
    - A class is *persistent*, if the values of their attributes hav ea
      lifetime beyond single execution. 
    - Examples: File systems, Databases. 

### Mapping an Object Model to a Database

- UML object models can be mapped to relational databases: 
    - Some degradation occurs because all UML constructs must be mapped to a
      table. 
    - Mapping of classes, attributes and associations
        - Each class is mapped to a table
        - each class attribute is mapped to a table-col
        - an Instance of a class represents a row
        - a many-to-many assocation is mapped to its own table
        - Methods are not mapped at all. 

ORMs exist, sadly. 

## Global Resource Handling

- Addresses access control
- Describes access rights for different classes of actors
- Describes how objects can be guarded against unauthorized access

### Defining Access Control

- In Multi-user systems different actors have different rights (users/admins) 
- How do we model this? 
    - during analysis we model access rights with usecases. 
    - during system design we model access by determining which objects are
      shared among actors. For this we introduce the *access matrix*

### Access Matrix

It models the access of actors on classes. Rows = actors, Cols = Classes to be
controlled. In general its a sparse matrix

There are three different implementation: 

- *Global Access Table*: Represents every non-empty cell in the matrix as
  triple `(actor, class, operation)`
- *Access Control List*: Associates a lost of `(actor, operations)` pairs with
  the class being accessed. Every time an instance of this class is accessed,
  the ACL is checked for the corresponding actor and operation
- *Capability*: Associates a `(class, operations)` pair with an actor. A
  capability allows an actor to gain controll access by calling one of the
  class operations

The *Proxy Pattern* can be used for access control, by using the proxy for access
verification before relaying. 

### Proxy Pattern 

- Access control ("Protection Proxy"): Checks access before relaying
- Caching of Information ("Remote Proxy"): Checks if call occured before
  relaying
- Stand-in ("Virtual Proxy"): Minimizes cost required for large objects by
  allowing access to parts.

## Software Control

2 choices: 

- Implicit Software Control: rule-based, logic programming
- Explicit Software Control: 
    - Centralised Control: Prodecdure-driven or event-driven
    - Decentralised Control: Control resides in independent objects: Messages, Actors, etc. 

### Centralised v decentralised Design

- Centralised Design: one subsystem controls everything ("Spider") Pro: Easy to
  change, Con: Bottlenecks.
- Decentralised Design: More than one control object. Pro: Fits nicely into
  OOP, Con: REsponsibility is spread out

## Boundary Condition

- Initialisation: Starting up 
- Termination: Clean up upon SIGKILL
- Failure: Shit breaks. 

### Modelling Boundary condition

Boundary conditions are best modeled as use cases. Actor is often the sysadmin

Interesting usecases: 

- Startup of subsystem/full system
- Termination of subsystem
- Error in subsystem

## Requirements Review

After done with elicitation, we write the technical spec, and we validate
requirements with client/user. 

### Requirement validation: 6 criteria: 

- Correctness: Requirement represents client's view
- Clarity: can only be interpreted one way
- Completeness: all possible ways of using the system are described
- Consistency: there are no requirements that contradict each other
- Realism: requirements are fulfillable.
- Traceability: Compoentns and behaviour can be traced to functional
  requirements. 

### Verfication vs Validation

- Verifcation is an equivalence check
- Validation is comparison with reality/the user's idea


