# The Practical Test Pyramid

It tell us how to group tests depending on the granularity, and how many test we should have in each group.

Production-ready software requires testing before it goes into production. Automating the tests allows to know whether the software is broken in a matter of seconds and minutes. Having an effective software testing approach allows teams to move fast and with confidence.

But, what should a well-rounded test portfolio look like to be responsive, reliable and maintainable?

## The Importance of (Test) Automation

Software is an essential part of the world we live in and it changes and increases every day. For that reason, new ways to deliver it faster without sacrificing its quality is required. **Continuous delivery**, a practice to automatically ensure that software can be released into production, can help you with that. With continuous delivery you use a build pipeline to automatically test your software and deploy it to your testing and production environments.

Building, testing and deploying an ever-increasing amount of software manually soon becomes impossible. Automating everything — from build to tests, deployment and infrastructure — is the only way forward.

|![](https://martinfowler.com/articles/practical-test-pyramid/buildPipeline.png)|
|:--:|
|Figure 1: Use build pipelines to automatically and reliably get your software into production|

Traditionally software testing was overly time-consuming manual work done by deploying your application to a test environment and then performing some black-box style testing.
Luckily there's a remedy for repetitive tasks: automation.

Automating your repetitive tests can be a big game changer in your life as a software developer.

- Avoids click protocols in order to check if your software still works correctly.
- Automation allows to change your codebase without batting an eye, large-scale changes and knowing whether you broke stuff within seconds is important.

## The Test Pyramid

It's a great visual metaphor telling you to think about different layers of testing. It also tells you how much testing to do on each layer. The original consists of three layers:

|![Figure 2: The Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid/testPyramid.png)|
|:--:|
|Figure 2: The Test Pyramid|

This pyramid is a little simplistic for today's standard and the naming of the layers can be quite misleading, but the concept is important:

- Write tests with different granularity
- The more high-level you get the fewer tests you should have

## The Sample Application

### Functionality
|METHOD|Endpoint| Description|
|:--:|:--:|:--:|
|GET|/hello| Returns the allowed operations (sum, sub and fac)|
|GET|/{operation}/{number_1, number_2}| Returns the result|
|GET|/{id}| Returns the operation saved on db|

### Unit tests

The foundation of your test suite will be made up of unit tests. Your unit tests make sure that a certain unit of your codebase works as intended. Unit tests have the narrowest scope of all the tests and the number of unit tests in your test suite will largely outnumber any other type of test.

|![](https://martinfowler.com/articles/practical-test-pyramid/unitTest.png)|
|:--:|
|Figure 5: A unit test typically replaces external collaborators with test doubles|

#### What's a Unit?

It depends, in a functional language a unit can be a single function. Each unit test will call a function with different parameters and ensure that it returns the expected values. In an object-oriented language a unit can range from a single method to an entire class.

#### Sociable and Solitary

When testing, we have two options:

- Solitary:
   all collaborators (e.g. other classes that are called by your class under test) of your subject under test should be substituted with mocks or stubs to come up with perfect isolation and to avoid side-effects and a complicated test setup.
- Sociable:
   Only collaborators that are slow or have bigger side effects (e.g. classes that access databases or make network calls) should be stubbed or mocked.

At the end of the day it's not important to decide if you go for solitary or sociable unit tests. Writing automated tests is what's important. 

#### Mocking and Stubbing

Mocks and Stubs are two different kinds of Test Doubles (there are more than these two). You can use test doubles to replace objects you'd use in production with an implementation that helps you with testing. This allows us to test small pieces of code in isolation and avoid hitting databases, the filesystem or firing HTTP queries to keep your tests fast.

- **Stubs**:
  provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test.
- **Mocks**:
  are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting.

#### What to Test?

The recommendation is to have one test class per production class.

#### Example

[Unit test](https://github.com/eguezgustavo/tdd_dojo/tree/Exercise_4/example_3/main_test.py)
### Integration Tests

Integration Tests test the integration of your application with all the parts that live outside of your application. For your automated tests this means you don't just need to run your own application but also the component you're integrating with.

There are several ways to do integration testing:

- To test through the entire stack of your application connected to other applications within your system. I like to treat integration testing more narrowly and
- To test one integration point at a time by replacing separate services and databases with test doubles. 

A database integration test would look like this:
|![](https://martinfowler.com/articles/practical-test-pyramid/dbIntegrationTest.png)|
|:--:|
|Figure 6: A database integration test integrates your code with a real database|

1. start a database
2. connect your application to the database
3. trigger a function within your code that writes data to the database
4. check that the expected data has been written to the database by reading the data from the database

Write integration tests for all pieces of code where you either serialize or deserialize data:

- Calls to your services' REST API
- Reading from and writing to databases
- Calling other application's APIs
- Reading from and writing to queues
- Writing to the filesystem

When writing narrow integration tests you should run your external dependencies locally or use a fake version of the real service.

Integration tests are on a higher level than unit tests. They have the advantage of giving you the confidence that your application can correctly work with all the external parts it needs to talk to.

#### Example: Database Integration

The OperationRepository is the only repository class in the codebase. 

To make it easier for you to run the tests on your machine our test connects to an docker database.


#### Example: Integration With Separate Services

[repository_test](https://github.com/eguezgustavo/tdd_dojo/tree/Exercise_4/example_4/api/test/repository)

### Contract Tests

The modern approach for software development is to spread the development of a system across different teams to build individual, loosely coupled services without stepping on each other toes and integrate these services into a big, cohesive system. Splitting systems into many small services means that these services need to communicate with each other via certain interfaces. These Interfaces can come in different shapes and technologies:

- REST and JSON via HTTPS
- RPC using something like gRPC
- building an event-driven architecture using queues

For each interface there are two parties involved: the provider and the consumer.

|![](https://martinfowler.com/articles/practical-test-pyramid/contract_tests.png)|
|:--:|
|Figure 7: Each interface has a providing and a consuming party. The specification of an interface can be considered a contract.|

As you often spread the consuming and providing services across different teams you find yourself in the situation where you have to clearly specify the interface between these services (the so-called contract). Companies have approached this problem in the following way:

- Write a long and detailed interface specification (the contract)
- Implement the providing service according to the defined contract
- Throw the interface specification over the fence to the consuming team
- Wait until they implement their part of consuming the interface
- Automated contract tests to make sure that the implementations on the consumer and provider side still stick to the defined contract.

In a more agile organization you should take the more efficient route. You should talk to the developers of the other services directly instead of throwing overly detailed documentation over the fence.

**Consumer-Driven Contract tests (CDC tests)** let the consumers drive the implementation of a contract. Using CDC, consumers of an interface write tests that check the interface for all data they need from that interface. The consuming team then publishes these tests so that the publishing team can fetch and execute these tests easily. The providing team can now develop their API by running the CDC tests. Once all tests pass they know they have implemented everything the consuming team needs.

|![](https://martinfowler.com/articles/practical-test-pyramid/cdc_tests.png)|
|:--:|
|Figure 8: Contract tests ensure that the provider and all consumers of an interface stick to the defined interface contract. With CDC tests consumers of an interface publish their requirements in the form of automated tests; the providers fetch and execute these tests continuously|

This approach allows the providing team to implement only what's really necessary.

### UI Tests

Most applications have some sort of user interface for example a web interface in the context of web applications, a REST API or a command line interface.

UI tests test that the user interface of your application works correctly. User input should trigger the right actions, data should be presented to the user, the UI state should change as expected.

Some tools to perform this test are Selenium, or Galen.

With web interfaces there's multiple aspects that you probably want to test around your UI: behavior, layout, usability or adherence to your corporate design are only a few. Modern single page application frameworks often come with their own tools and helpers that allow you to thoroughly test these interactions in a pretty low-level (unit test) fashion.

### End-to-End Tests

Testing your deployed application via its user interface is the most end-to-end way you could test your application. 


|![](https://martinfowler.com/articles/practical-test-pyramid/e2etests.png)|
|:--:|
|Figure 9: End-to-end tests test your entire, completely integrated system|

End-to-end tests (also called Broad Stack Tests) give you the biggest confidence when you need to decide if your software is working or not.

End-to-End tests come with their own kind of problems:

- Who's in charge of writing these tests. Since they span multiple services (your entire system) there's no single team responsible for writing end-to-end tests.
- End-to-end tests require a lot of maintenance and run pretty slowly.
- this would require to start all your microservices locally as well. Good luck spinning up hundreds of applications on your development machine without frying your RAM.

Due to their high maintenance cost you should aim to reduce the number of end-to-end tests to a bare minimum.

Think about the high-value interactions users will have with your application. Try to come up with user journeys that define the core value of your product and translate the most important steps of these user journeys into automated end-to-end tests.

Remember: you have lots of lower levels in your test pyramid where you already tested all sorts of edge cases and integrations with other parts of the system. There's no need to repeat these tests on a higher level.

**User Interface End-to-End Test**
For end-to-end tests Selenium and the WebDriver protocol are the tool of choice for many developers. 

Example:

[end2end_test.py](https://github.com/eguezgustavo/tdd_dojo/tree/Exercise_4/example_4/api/test/end2end/end2end_test.py)


**REST API End-to-End Test**
Avoiding a graphical user interface when testing your application can be a good idea to come up with tests that are less flaky than full end-to-end tests while still covering a broad part of your application's stack. 

### Acceptance Tests — Do Your Features Work Correctly?

The higher you move up in your test pyramid the more likely you enter the realms of testing whether the features you're building work correctly from a user's perspective. You can treat your application as a black box and shift the focus in your tests from

when I enter the values x and y, the return value should be z

towards

given there's a logged in user

and there's an article "bicycle"

when the user navigates to the "bicycle" article's detail page

and clicks the "add to basket" button

then the article "bicycle" should be in their shopping basket

Sometimes you'll hear the terms functional test or acceptance test for these kinds of tests. At one point you should make sure to test that your software works correctly from a user's perspective, not just from a technical perspective. What you call these tests is really not that important. Having these tests, however, is. Pick a term, stick to it, and write those tests.

Example:

```py
# a sample acceptance test in Python

def test_add_to_basket():
    # given
    user = a_user_with_empty_basket()
    user.login()
    bicycle = article(name="bicycle", price=100)

    # when
    article_page.add_to_.basket(bicycle)

    # then
    assert user.basket.contains(bicycle)
```

### Exploratory Testing

It is a manual testing approach that emphasizes the tester's freedom and creativity to spot quality issues in a running system. Simply take some time on a regular schedule, roll up your sleeves and try to break your application. After that, you can automate most of your findings to make sure there won't be any regressions of that bug in the future.

### Putting Tests Into Your Deployment Pipeline

With Continuous Integration or Continuous Delivery, you'll have a Deployment Pipeline in place that will run automated tests every time you make a change to your software. Usually this pipeline is split into several stages that gradually give you more confidence that your software is ready to be deployed to production and give us Fast Feedback of the code that we are writing.

### Avoid Test Duplication

Writing and maintaining tests takes time. Reading and understanding other people's tests takes time. And of course, running tests takes time.

As with production code you should strive for simplicity and avoid duplication. In the context of implementing your test pyramid you should keep two rules of thumb in mind:

- If a higher-level test spots an error and there's no lower-level test failing, you need to write a lower-level test
- Push your tests as far down the test pyramid as you can

### Writing Clean Test Code

Here are some more hints for coming up with maintainable test code before you go ahead and hack away on your automated test suite:

- Test code is as important as production code. Give it the same level of care and attention. "this is only test code" is not a valid excuse to justify sloppy code
- Test one condition per test. This helps you to keep your tests short and easy to reason about
- "arrange, act, assert" or "given, when, then" are good mnemonics to keep your tests well-structured
- Readability matters. Don't try to be overly DRY . Duplication is okay, if it improves readability. Try to find a balance between DRY and DAMP code
- When in doubt use the Rule of Three to decide when to refactor. Use before reuse





