# Overview, EIST, #1
In this Lecture, we introduce the concepts found in software engineering and
see if we can't draw something useful from this whole mess. Length, 140
minutes. Time to skip around. 

# Content
## Modelling
Models abstract reality and approximate it in some incomplete sense we can deal
with. Differentiation: 

- _Object Model_: What is the structure of the system? 
- _Functional Model_: What are the functions of the system? (What does it do?)
- _Dynamic Model_: How does the system react to external events? 

Other Models are used to manage Software System Development. 

- Task Model
    - PERT Chart: Describes the dependencies between development activities
    - Schedule: Describes how the activities can be accomplished to finish a
      project before a deadline
    - Organisation Chart: Describes the roles of each participant in the project. 
- Issue Model
    - What are the open issues? 
    - What proposals do we have to close the issue? 
    - What resolutions can be made? 

Why is Software development difficult? 

- The Problem usually ambiguus
- The requirements are usually unclear and change once becoming clearer
- The Problem domain (Also called application domain) is complex, and so is the
  solution domain.
- The development process is difficult to manage. 
- Software offers extreme flexibility. 

## Software engineering: A problem solving activity

- Analysis: Understand the nature of the problem and break the problem into pieces
- Synthesis: Put the pieces together in a large structure. 

For Problemsolving we use techniques, methodologies, and tools. 

## Techniques, Metholodlogies and Tools

- Techniques: Formal precedures for producing using some well defined notation, like
  sorting algs. 
- Methodologies: Collection of techniques applied across software development and unified by
  a philosophical approach, for example OOP Analysis and Design.
- Tools: Instruments or automated systems to accomplish a technique like an editor
  or IDEs etc. 

## Computer science vs. Engineering
- The Computer Scientist 
    - Assumes techniques and tools have to be developed
    - proves theorems about algorithms
    - Designs languages and grammars
    - Has, in theory, infinite time
- The engineer
    - Develops a solution for a problem formulated by a client
    - Uses Computers and languages, techniques and tools
- The Software Engineer
    - Works in multiple application domains
    - Only has limited time
    - Changes occur often, and you have to adapt.

## Definition of Software Engineering

Software Engineering is a collection of techniques, methodologies and tools
that help with the production of a _high quality_ software system developed
with a given _budget_ before a given _Deadline_ while _change_ occurs.

## Dealing with Complexity

- Modeling
- Notations (UML, OCL) 
- Requirements elicitation
- Anlysis and Design (OOSE, scenario-base design, formal specs) 
- Implementation
- Testing. 

There are three ways to deal with Complexity: 

- Abstraction
- Decompositon
    - Functional Decompositions (turn it into functions)
    - OOP Decompotions (turn it into objects and their relations) 
- Hierarchy

## Dealing with Change

- Release Management (CI/CD) 
- Delivery
- Software Life Cycle Meeting
- Rationale Management
- Project Management. 

## Class Identiication and Project Types
Basic Assumptions: 

- We can find _classes for a future system_: Greenfield Project
- We can identify classes in an existing system: Reengineering Project
- We can create a class-based interface to an existing system: Interface
  Engineering Project. 

## Phenomenon vs Concept

- A _Phenomenon_ is an object in the world of a domain as you perceive it. 
- A Concept describes the common properties of phenomena. It is a three-tuple: 
    - Name: Distinguishes from other concepts
    - Purpose: Properties that determin concept-membership
    - Members: Phenomena which exhibit all properties required.

An _Abstraction_ is the classifications of phenomena into concepts, while
_Modeling_ is the development of abstractions to answer specific questions about
a set of phenomena while ignoring irrelevant details. 

## Systems
A system is an organized set of communicating parts. 

- A _view_ depicts selected aspects of a model


## Summary

- Software engineering is _problem solving_ 
- We need to talk to the customer and domain experts to identify the problem to
  be solved, or "elicit requirements" 
- Some problems are impossible to solve, other only after changing or
  reinterpreting the requirements
- Software engineering is about dealing with change and complexity while trying
  to solve the problem
- Software engineering uses methods like divide and conquer and tools to solve
  problems

## Odds and Ends I need to remember

- Non-functional requirements are constraints, ie, "The system must respnd in
  less than 400ms and be written in Java".
