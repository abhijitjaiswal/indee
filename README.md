# indee
Functional Test for login.

Requirement: Versions >= Python 3.4, >= Django 1.9, >= configparser 3.5, selenium, chromedriver
Browsers supported: Chrome, Firefox

By default test runs on Chrome, to change the browser to Firefox. change the following in config.txt:
"browsertype=Chrome" to "browsertype="

Also, before running the test please add username and password in config.txt file against parameter, "user" and "passwd" else the test will always fail.


Once above all conditions are met, change directory to "indee" folder and run the following.
python manage.py test

Sample Output:

C:\Python34\Scripts\indeeproject>python manage.py test
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 71.577s

OK
Destroying test database for alias 'default'...
