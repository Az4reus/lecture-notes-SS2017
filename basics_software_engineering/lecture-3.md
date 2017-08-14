# Overview, EIST #3
Roadmap for today: 

- UML is an extensible language: Predefined types and Stereotypes.
- Requirements Analysis and Stakeholders

After today I will ostensibly be able to: 

- create different types of objects with stereotypes
- the difference between different types of requirements
- use different techniques to describe requirements
- understand requirements review and requirements documents. 

# Content

In EIST, finite-state-automata are always deterministic. 

## Extending UML: Stereotypes

Stereotypes allow you to extend the vocabulary of the UML so that you can
create new model elements, drived from existing ones. These can be represented
textually (for example, `<<Control>>`, `<<Entity>>`, etc.) as well as
graphically, for example:  

- **Entity Objects** rerpesent the persistent information tracked by the system
  (application domain objects, also called "Business Objects" (kill me))
- **Boundary Objects** represent the interaction between user and system. 
- **Control Objects** represent the control tasks to be performed by the system

Other stereotypes that will become important: 

- Subsystems: `<<interface>>`
- Stereotypes for classifying method behaviour: `<<constructor>>`,
  `<<getter>>`, etc

A **System Model** consists of a functional, object and dynamic model. The
centre of that is the object model, the rest are supporting.


## Requirements Engineering

- Requirements: Elicitation Definition of the system in terms understood by a
  customer or user. Results in *Requirements Spec*
- Analysis: Definition of the system in terms understood by a dev. Results in
  the *Analysis model*, also called *Technical Spec* or "*Lastenheft*"
- Requirements Engineering: Combination of the two activities, elicitation and
  analysis. *An activity that defines the requirements of the system under
  construction.*

The **Requirements Spec** is informal and in natural language, the **analysis
model** is written in semi-formal languages. Like UML or Z/VDM.

Parts of formal requirements: 

- Functionality
- User Interaction
- Error Handling
- Environmental conditions (interfaces) 

**Not** part of formal requirements: 
 
- System Design
- Implementation technology
- Development methodology. 

Typical Software cycle: 

- Application Domain: 
    - Requirements Elicitation
    - Analysis
- Solution Domain:
    - System Design
    - Object Deisgn 
    - Implementation
    - Testing
- Maintenance and Delivery/Evolution/CD

## Questions that need to be answered during Requirements Elicitation

- How can we identify the *purpose* of a system? What are the requirements, what
  are the *constraints*? 
- How can we *identify* the system boundary? What's *inside*, and what isn't?
  Defining this is often difficult. 

## Quality Requirements
URPS = Usability, Reliability, Performance, and Supportability.

- Usability: For example, response time, start-up times, average downtime, etc. 
- Reliability: Uptime, support required.
- Performance: Not squandering Resources, being somewhat efficient
- Supportability: Ability to patch the product, and fix it easily. Like binary
  patching, vs requiring reinstall. 
