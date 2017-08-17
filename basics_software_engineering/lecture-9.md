# Overview, EIST #9

## UML statechart diagram

Syntax: 

- UML state charts are a form of FSA, with the syntax being: 
  - Events in boxes
  - State changes expressed as arrows
  - Arrows have denoting text according to this rough grammar: 
      - `Event(parameter) [condition]/activity`
      - Event/parameter works like unapply
      - condition is a boolean guard
      - activity is what is to be done when the guard is true and the event
        happens to transition to a new state

## Mapping contracts to java

- Breaking a contract is expressed as throwing an exception, while pre/post
  asserting and checking invariants. 

## Today: Lifecycle modelling. 

- Models: 
    - Sequential: Waterfall, V-Model
    - Iterative: Boehm's spiral model, Unified process. 
    - entity: scrum. 
- Defintion: Set of activities and their relationships to each other to support
  development of a system. 
- IEEE 1074 lifecycle process groups:
    1. **Lifecycle Modeling:** Selection of a lifecycle model
    2. **Pre-Development:** Concept exploration, System allication
    3. **Development:** Requirements, Design, Implementation
    4. **Post-Development:** Installation, Operation & Support, Retirement. 
    5. **Cross-Development (Integral Processes):** Verifcation & Validation,
       Configuration Management, Documentation, Training. 
    6. **Project Management:** Project Initiation, Monitoring & Control, Software
       Quality Management.
- Tailoring: There's no one-size-fits-all software lifecycel model that works
  for all possible projects. So you tailor, and change the name of activities,
  or discuss which to keep and which to cut and in wht order to do them. 
- Procedural models like Waterfall and V-model are not practiced that much
  anymore or even that useful. 
- Unified Model: what a clusterfuck. It can be understood as a generalisation
  of waterfall, where you allocate resources as needed with a specific focus
  (that, if taken in the extreme, leads to waterfall) to get the project done. 

_Discussion of scrum basics follows here, omitted due to previous knowledge
from work._ 
