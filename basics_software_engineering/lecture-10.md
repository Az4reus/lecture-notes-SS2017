# Overview, EIST #10

## Today: Configuration Management and Release Management. 

- Why Software Config management?
    - Collarboration begets problems, more than one version of the software has
      to be supported (legacy, beta, etc) 
    - Need for coordination -> SCM
- What is SCM? 
    - A set a management discipline within a software engineering process to
      develop a baseline
    - SCM encompasses the disciplines and technoqies of controlling change to
      software. 
- SCM Activities
    - Configuation item identification
    - Change management
    - Promotion management
    - Branch management
    - Release management
    - variant management. 
    - => No fixed order
- SCM Actors
    - Config Management: Responsible for identifying change items, defines
      procedures for releases
    - Change control board member: responsible for approving/rejecting changes
    - Developer: Develops and makes changes
    - Auditor: Making sure everything is consistent and complete. 

## Config item idenfitication

- Def: Config Item:  
  Aggregation of hardware, software, or both, designated for configurration
  management and treated as single entity in SCM. 
- Anything that might change and influence the project is a Config Item. 
- Def: Baseline:  
  Formal spec that has been reviewed and agreed to by stakeholders. 

## Change Management

- A baseline can only be changed through a change request procedure. 
- Change management is the handling of these requests. 
- The purpose of a _change policy_ is to guarantee that each promotion or
  release conforms to commonly accepted criteria, for example, "No release may
  have compiler warnings or errors."

## Branch Management

- Types of Baseline are for example _Product Baseline, Developmental Baseline,
  or a Functional baseline._ 

## Release Management. 

- Large and distrubeted software projects need to provide a development
  infrastructure with an integrated build management that supports: 
      - Regular builds from the master directory. 
      - Automated execution pf tests
      - Email notification
      - Determination of metrics. 
      - Auomated publishingof the application and results of tests. 
