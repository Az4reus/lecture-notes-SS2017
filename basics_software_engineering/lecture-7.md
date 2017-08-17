# Overview, EIST #7
In this Lecture, we.... 

# Content

## Patterns, continued
### Observer Pattern

- Problem: We have an object with freuqnetly changing states
- We want to provide multiple views to the same object
- Requirements: System should require consistency across views.
- Should be extensible. 

Enter: The Observer pattern! 

- Models a 1-to-n dependecy between objects, connects state of an observed
  object with the subject with many observers
- Usage: 
    - Maintaining consistency across redundant states
    - Optimising a batch of changes to maintain consistency
- This is also called **Publish And Subscribe** (Oooh. Well that makes it
  simple)
- The subject represents the entity in question
- Observers attach to the subject by calling `subscribe`. 
- Upon notification, observers pull new data, or get pushed new data. 

Three variations here: 

- **Push notification.** `notify` is triggered upon update. 
- **Push-update Notification:** Data is included in `notify` call. 
- **Pull Notification:** Observer periodically pulls data from Subject

## Pattern Oriented Development

- Ideally everything should be covered by a pattern. (Fuck me, no.) 


*The rest of this is example-development of a bumper-car game, with live
modeling and programming in class*
