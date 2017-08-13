# Overview, EIST #2
In this Lecture, we model shit in UML. Wheee. 
A first pass on functional modeling, object modeling, dynamic modeling. 
At the end of the lecture I am supposed to be able to:

- describe a use-case diagram that models common functionality and extensions. 
- describe a class diagram with multiple classes and different types of
  associations. 
- apply Abott's textual analysis technqiue to create class diagrams from a
  problem statement given in natural language. 
- describe a dynamic model for a single object with dynamic behaviour
- describe a dynamic model for a workflow involving several objects. 

# Content

- Application domain, def: The environment in which the system is operating. 
- Solution domain, def: The tech used to build the system.

UML we will need: 

- Use case diagrams
    - Use-case diagrams depict functionality inside a system taken advantage of
      by actors. 
- Class diagrams
    - This is known.
- Sequence diagrams
    - Sequence diagrams describe the time-flow between components that happen
      when you use a certain functionality. 
- Statechart diagrams
    - Represent the dynamic behaviour of a single object. like a FSA but more
      generalised and UML 

Generally speaking, use-case diagrams are used for the _functional model_,
class diagrams for the _object model_ and sequence- and state diagrams for the
_dynamic model_. 

In UML, an _Actor_ is an external role that represents a specific role in the
system that users can be generalised into. 

Usecases can be related: 

- `<<extends>>` Relationship typcially models a rarely-used use case or
  exceptional functionality.
- `<<includes>>` typically models behaviour that is more common than one
  use-case and is thus contained by others. 

Difference between _Composition_ and _Aggregation_ in UML is that a composite
implies its children do not exist on their own, but only as part of the
composite. Buttons on a machine do exist on their own, but make little sense to
model, vs. tyres on a car. 

**Review Homrwork for state-chart diagrams et al.**


