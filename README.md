# **Sprint3**

## **OBJECTIVE**

Create multi-stage pipeline having Beta/Gamma and Prod stage using CDK. Deploy the project code in 1 Region. Each stage must have bakeTimes, code-review, and test blockers. Write unit/integration tests for the web crawler. Emit CloudWatch metrics and alarms for the operational health of the web crawler, including memory and time-to-process each crawler run. Automate rollback to the last build if metrics are in alarm. Manage README files and runbooks in markdown on GitHub.

## **TECHNOLOGIES USED**
### **1	VS CODE**

The coding and development environment	

### **2	AWS CLoudWatch**
To monitor metrics on the stack that we begun with 

### **3	AWS Management Console**
To access and interact with the deployed lambda functions.

### **4	Github**
For Version Control and Collaboration, particularly peer reviews.

## **SPRINT BREAKDOWN**

### **Task – 1: Create an environment**
A development environment was created by making a copy of the sprint2 stack files since this tasks builds on top of the previous one.

### **Task – 2: Make Pipeline Stack and Stage**
The CI CD pipeline and its code needs to be in a separate file. The pipeline stack is at the same hierarchical level with the sprint3stack whereas the pipeline stage is on top of the two.

### **Task – 3: Define Beta, Gamma and Prod Stages and Their respective tests**
For the beta stage I resorted with doing unit tests, whereas at the gamma stage I resorted with doing functional tests. These need to be manually approved in the pre-production level before they are made a part of the newer version.

### **Task – 4: Automate LambdaFunction and Metric Creation**
Parts of the lambda function and metric uploads to the cloud that were created in the Sprint2 are automated in order to make our pipeline function the way it is supposed to.

### **Task – 5: Testing and Rollbacks**
Automated testing needs to be performed with additions that need to be made to the test folder. These test files ensure that required tests are performed before all git push commands are executed.

## **ISSUES/ERRORS AND TROUBLESHOOTING**

**Description:** error parsing the events in lambda_handler.
[‘Resources’] could not be parsed from the event in the DynamoDB lambda function that was used from the previous sprint code
**Solutions:**  I commented out this portion as it wasn’t needed for this particular task.

**Description:** Github authentication failed
**Solutions:** Create a Private Access Token and use it for the password to login to the github rep. 



