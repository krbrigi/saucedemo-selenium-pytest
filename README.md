# SauceDemo Selenium Project
[![Test Project Saucedemo](https://github.com/krbrigi/saucedemo-selenium-pytest/actions/workflows/tests.yml/badge.svg)](https://github.com/krbrigi/saucedemo-selenium-pytest/actions/workflows/tests.yml)
[![Static Badge](https://img.shields.io/badge/Report-Allure-orange)](https://krbrigi.github.io/saucedemo-selenium-pytest/)

## Project overview
This project is an automated test framework for the SauceDemo web application.

It was developed as part of my software testing portfolio using Python, Selenium WebDriver and Pytest, following the Page Object Model (POM) design pattern.

## Technologies
- Python
- Selenium
- Pytest
- Page Object Model (POM)
- Allure Report
- GitHub Actions


## Application under test
https://www.saucedemo.com/

## Implemented tests

- Login tests
- Invalid login scenarios
- Product inventory tests
- Shopping cart tests
- Checkout process
- End-to-end purchase flow

## Project architecture

The framework follows the Page Object Model (POM) design pattern to keep page interactions separated from test logic, making the tests easier to maintain and extend.

Project structure:
- pages - Page Object classes
- tests - test cases
- utils - helper functions

## How to run tests
```bash
pip install -r requirements.txt
pytest
```

## Allure report
Generate and open the report
```bash
allure serve allure-results
```

## Continuous Integration
The project uses GitHub Actions to automatically run the test suite:
- after every push
- for every pull request
- on a daily scheduled run at 6:00 PM

## Planned improvements

- Extend negative test scenarios
- Cross-browser testing
