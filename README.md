# Numeric password cracker

A python 2.7 program for cracking a numeric password on a website

I wrote this back in 2017 after losing my password to my universitys online registration site.
Unfortunately for me, the password recovery process is far from easy, mostly  because the online registration system is quite old. This age of course had a silver lining. The system had no protection against multiple failed login attempts.
The passwords were numeric and maximum lengths also restricted.

Using the selenium web driver

1. The program opens a web page
2. Finds the login form
3. Inputs details
4. Clicks the login button
5. Checks to see if the password worked
6. If it didnt, the program navigates back and tries another password
7. Repeats till it finds the password
