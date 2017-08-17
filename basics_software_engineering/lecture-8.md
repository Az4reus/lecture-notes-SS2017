# Overview, EIST #8
In this Lecture, we.... 

# Content
## Specifying Interfaces

1. Interface specification during *requirement analysis*
    - Identification of attributes and operations
    - No need to specify types or parameters\
2. Interface specification during *object design*
    - Add type signature information
    - Add visibility information
    - Add contracts. 

## Modeling Constraints with Contracts

- Functional requirements addressed during analysis: They can be modeled with
  use cases and class diagrams and so on
- Nonfunctional requirements are addressed during system design
- Contraints are addressed during object design: There are constraints which
  cannot be modeled in UML

## Design by Contract

- DbC is a detailed object design approach
- It allows a formal interface specification for software compoentns: A
  collection of preconditions, postconditions and invariants
- Term comes from Bartrand Meyer, creator of Eiffel

## OOP Contracts

- An OOP contract describes the services that are provided by an object. For
  each service it describes two things: 
    1. The conditions under which the service will be provided
    2. A specification of the result of the service that is provided.
- A breach of these conditions will result in an exception

## Modeling OOP Contracts

- Natural Language
- Mathematical Language
- OCL: Object Constraint Language
    - Design Goals: a language for the formulation fo constraints with the
      easiness of ntural langauge and formal strength of the mathematical
      notation. \
    - OCL is based on the predicate calculus

## OO-Contract

- An OO contract is an exact specification of the interface of an object. A
  contract includes three types of predicates: 
    - Invariant: A predicate that is always true for all instances of a class. 
    - Precondition: A predicate that must be true before an operation is
      invoked. 
    - Postcondition: A predicate that must be true after an operation is
      invoked. 
- A contract is called a formal specification if the invariatns, preconditions
  and postconditions in the contract are unambiguous.

## Why not use Contracts in Analysis? 

- Customer might not understand formal constraints
- LEvel of detail vs rate of requirements change can change frequently leading
  to massive overhead of managing contracts. 

## Introducing OCL

- OCL: A formal language for expressing *constraints* over a set of objects in
  a model. 
- Rough OCL grammar because I'm bored: 

```
constraint := class::function condition
condition := (inv: expr|pre: expr|post: expr)
expr := attribute operator attribute
operator := not|implies|exists|is|<|>|<=|>=
attribute := function|class->function|expr@qualifier|self.attribute
qualifier := pre|post
```

Examples: 

```
context Person inv: self.age >=0
context Person inv: self.parents->forAll(e|e.age>self.age)
context Person::hasBirthday() post: self.age=self.age@pre+1
context Person inv: self.parents->size()<=2
context Person::getsChild() post: self.childs->notEmpty() and
    self.childs->size() > self.childs@pre->size()
context Person inv: self.age<18 implies self.cars->isEmpty()
context Auto inv: self.registration>=self.constructionYear
context Person inv: self.cars->notEmpty() implies self.cars->exists( a | Calendar.YEAR
    - a.constructionYear < self.age)
context Person inv: self.parents->excludes(self)
context Person inv: Person.allInstances()->exists(p | p.cars->size() > 0)
```

## When should you refactor models or code?

1. There's a problem in the system model $\Rightarrow$ Model Refactoring
2. There's a problem in the code (Also called _code smell_) $\Rightarrow$ Code
   Refactoring 
