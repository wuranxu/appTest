__author__ = 'Woody'
import unittest


class result(unittest.TextTestResult):
    successes = []
    failures = []
    errors = []

    def addSuccess(self, test):
        case_id = test.case_id
        if case_id not in self.successes:
            self.successes.append({case_id: test})

    def addFailure(self, test, err):
        case_id = test.case_id
        if case_id not in self.failures:
            self.failures.append({case_id: test, "msg": err})

    def addError(self, test, err):
        case_id = test.case_id
        if case_id not in self.errors:
            self.failures.append({case_id: test, "msg": err})

    def printErrorList(self, flavour, errors):
        pass

    def printErrors(self):
        pass