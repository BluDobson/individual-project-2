# Song Generator

## Contents
* [Introduction](#Introduction)
* [Design](#Design)
    * [Risk Assessment](#Risk-Assessment)
    * [Trello Board](#Trello-Board)
    * [Application Diagram](#Application-Diagram)
    * [CI Pipeline](#CI-pipeline)
* [Development](#Development)
* [Review](#Review)

---
## __Introduction__

The objective of this project is to create a service-orientated architecture for my application, creating four services that work together. As well as two iterations of the three services used to create information.

_Service 1:_
* The application that users will interact with, which will be a simple page displaying the information pulled from the other services.

_Service 2:_
* This service will simply generate an artist or an album from a list and return it.

_Service 3:_
* This service will generate a random string of characters with a different length depending on the iteration.

_Service 4:_
* This service will generate a song based on the information generated from Service 2 and Service 3.

I will be creating these different implementations as different versions of the application to demonstrate how a rolling update can be performed.

I'll be using a variety of tools during the design process, as well as CI/CD tools to ensure that the application can be deployed easily without requiring further configuration.

---
## __Design__
### __Risk Assessment__
Here is the first draft of my risk assessment, showing all the potential issues I could run into during development of the project, I plan to add other issues, and review the solutions I decided to implement once the project is finished.

![first draft risk assessment](./images/FDRA.png)

The full risk assessment can be found [here](https://qalearning-my.sharepoint.com/:x:/g/personal/bdobson_qa_com/EVedzs3PfnVDh8thRQIWPDwBybsifzJtpsUZghWReMfN9Q?e=lHYxoL)

---
### __Trello Board__
Once again I decided to use Trello to track my progress during the project.

![trello board](./images/Trello.png)

The complete board can be found [here](https://trello.com/b/Ptseqgzs)

---
### __Application Diagram__
I decided to create an application diagram, to show how the different services will interact to create the application. 

![app-diagram](./images/App-Diagram.png)

---
### __CI pipeline__
Finally, I created a diagram to show the CI pipeline I plan to create with the application.

![CI-pipeline](./images/CI-pipeline.png)

---
## __Development__