## TestingBot - Behave

TestingBot provides an online grid of browsers and mobile devices to run Automated tests on via Selenium WebDriver.
This example demonstrates how to use Python with Behave to run a test in parallel, across several browsers.

### Environment Setup

1. Setup
    * Clone the repo
	* Install the dependencies `pip install -r requirements.txt`

2. TestingBot Credentials
   	Add your TestingBot Key and Secret as environmental variables. You can find these in the [TestingBot Dashboard](https://testingbot.com/members/).
    ```
    $ export TB_KEY=<your TestingBot Key>
    $ export TB_SECRET=<your TestingBot Secret>
    ```

### Running Tests

* To run a single test, run `paver run single`
* To run parallel tests, run `paver run parallel`

You will see the test result in the [TestingBot Dashboard](https://testingbot.com/members/)

### Resources

##### [TestingBot Documentation](https://testingbot.com/support/)

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)

##### [Behave Documentation](https://behave.readthedocs.io/en/latest/)
