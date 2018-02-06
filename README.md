# Chalice Testing Examples

This project contains examples for testing Chalice applications at both a **unit** and
**integration** level. These examples are just the best way that I have found to test
Chalice applications and **are in no way endorsed by the Chalice project**.

## Quick Start
```bash
$ git clone https://github.com/nplutt/chalice-test-examples.git
$ cd chalice-test-examples
$ mkvirtualenv chalice-test-examples
$ pip install -Ur requirements.txt -Ur extra_requirements.txt
```

## Unit Tests
This example has been kept very simple as I don't think this is something most people
have issues with. The code can be found [here](https://github.com/nplutt/chalice-test-examples/blob/master/test/unit/test_app.py).

#### Running Unit Tests
```bash
$ pytest test/unit
``` 


## Integration Tests
The integration tests utilize Chalice's `LocalGateway` class, which is 
used to create the event for an application when running locally. This allows you to 
construct pretty simple tests that test the application from end to end. The code can
be found [here](https://github.com/nplutt/chalice-test-examples/blob/master/test/integration/test_app.py).

#### Running Integration Tests
```bash
$ pytest test/integration
```  

