# Overview, EIST #6

## Purpose of Object Design (Spoiler: Code reuse)

- Preparation of model for implementation.
- Transform and Optimise system model
- Investigate alternative ways to implement models
    - Use design goals for guidance
- Object design serves as the basis of implementation.

Object Design closes gap between Analysis and System Design, between
Requirements and the model

### Terminology: Naming of Design Activities
Methodology: Object-oriented software engineering (OOSE)

- System Design: Decomposition into subsystems and services
- Object Design: Datastructures & Algorithms
- Implementation: Language is chosen

Methodology: Structured analysis/design

- Preliminary Design: Decompostion and datastructures
- Detailed Design: Algorithms, Language, and Datastructures refined

## Object Design Activities

OD consists of 4 Activities

1. Reuse: Identification of existing solution: Inheritance, design patterns,
   off-the-shel solutions
2. Interface Specification: Describes each class interface
3. Object model restructuring: Transforms the OD model to improve
   understadnability and extensibility.
4. Object model optimisation: transforms the OD model to address design goals
   and optimise.

### Identify Components

1. Identigfy missing components in the design gap
2. Make a build or buy decision to obtain missing components

$\Rightarrow$ Component-Based Software Engineering: 
The design gap is filled with existing components ("0% programming")

### Modeling the Real world

- Modelling the real world leadds to a system that reflects today's realities
  but not necessarily tomorrow's 
- There is a need for *reuseable and extendable* designs, also called flexible.

## Types of Reuse

- Reusing existing classes/interfaces
- Reuse existing knowledge (previous experience)

2 techniques to close the gap by reuse: 

1. Composition (also called Black Box Reuse)
2. Inheritance (also called White Box Reuse)

## The Use of Inheritance in OOSE

- Inheritance is used to achieve: 
    - Description of Taxonomies: Used during requirements analysis
        - Acitivity: Identify application domain objects that are
          hierarchically related
        - Goal: Make analysis object model more understandable
    - Interface specification: 
        - Activity: Identify the signatures of all identified objects
        - Goal: Increase reusability, enhance modability and the extensibility.

### Interface Spec through Inheritance and Delegation

- Implementation Inheritance: Subclassing from an implementation, re-using the
  functionality
- Delegation: Catching an operation and sending it to another object where it
  is already implemented, reusing that. 
- Specification Inheritance: Subclassing from a spec, which is abstract, but we
  can take advantage of the interface. 

**Strict Inheritance** is inheritance without overriding, IE only adding new
methods, not changing the old ones.

In Inheritance, **Contraction** is overriding methods of the super-class with
empty bodies in order to make them "invisible". 

### Conclusion: Inheritance in Analysis and Object Design: 

- Inheritance can be used during analysis as well as during object design
- Starting point is always the requirements-elicitation phase, we start with
  use cases and find existing objects
- Then we investigate the relationship between these objects ("discovering
  associations")
    - general associations
    - Aggregation/Composition
    - Inheritance
- During analysis, Inheritance is used to describe taxonomies
- During object design, inerhitance is used for interface specification adn
  reuse. 

## Discovering Inheritance Association

- To "discover" inheritance association we can proceed in two ways, called
  _Generalisation_ and _Specialisation_
    - Generalisation: Generalising the concrete class to find the super-class
    - Specialisation: Specialising a general concept to find the concrete
      class.

## Frameworks

- A **Framework** is a partial application that can be specialised to produce
  custom applications
- the key benefits fo frameworks are reusability and extensibility:
    - Reusability leverages the application domain knowledge and prior effort
      fo experienced devs
    - Extensibility is provided by methods which can be override by the
      application to extend the framework.

### White- and Black-box Frameworks

- Whitebox frameworks achieve extensibility through inheritance and dynamic
  binding, and providing specific hook methods
- Blackbox frameworks achieve extensibility by defining interfaces fro
  components that can be plugged into the network, integration happens via
  _delegation_. 

## Design Patterns
Originated in Architecture. Invented by Christopher Alexander. Then the gang of
four came and wrote their book. 

### Three types of patterns: 

- Structural Patterns: 
    - Reduce coupling between two or more classes, 
    - introduce an abstract class to eneable future extensions, 
    - encapsulate complex structures
- Behavioural Patterns: 
    - Allow a choice between algorithms, 
    - allow the assignment of responsibilities to objects, 
    - model complex control flows that are difficult to follow at runtime
- Creational Patterns: 
    - Allow to abstract from complex instantiation processes,
    - make systems independent from the way its objects are created, composed
      and represented. 

### Composite Pattern
- Observation: Many problems can be solved by modeling them as hierarchies. 
- Solution: The Composite Pattern lets a client treat an individual class
  called Leaf and the compositions of Leaf _uniformly_ (Think much like
  applying `map` to a functor ripples down to all elements contained therein.)

### Strategy Pattern
- Problem: Different Algorithms exist for a specific task. We want to be able
  to switch between these at runtime. (e.g. sorting lists for various sizes)
- Solution: Abstract the implementation behind an interface, where the
  different algorithms are implemented in various classes implementing the
  abstracted interface, and then one is able to switch between them based on
  context by use of a policy-manager.

### Bridge Pattern
- Problem: Many design decisions are made final at design time or at compile
  time. Sometimes its desirable to delay this until runtime. 
- The Bridge Pattern allows both, the implementation and the abstraction to
  vary independently from one another. This is done by making the abstraction
  and the client an interface, then one can specialise them independently.
- Using the Bridge Pattern allows us to provide multiple implementation under
  the same interface, much like the strategy pattern without a policy manager.
  This is useful especially when components are incomplete, not yet known, or
  unavailable. 


### Adapter Pattern
- The Adapter Pattern connects incompatible components by having a delegate of
  one type, and providing the Interface the other component expects, and
  translating the calls one expects to the interface the other one provides. 


### Observer Pattern
