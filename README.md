# indee
Functional Test for login.

Requirement: Versions >= Python 3.4, >= Django 1.9, >= configparser 3.5, selenium, chromedriver
Browsers supported: Chrome, Firefox

Change directory to "indee" folder and run the following. By default test runs on Chrome, to change the browser to Firefox. change the following in config.txt:
"browsertype=Chrome" to "browsertype="

# python manage.py test

The username and password are hardcoded in the test, but can be used in the similar way as browsertype is used.
