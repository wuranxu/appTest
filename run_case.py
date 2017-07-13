__author__ = 'Woody'

import unittest
from TestResult.Result import result
from TestSuite.MainActivity.Case001User import Case001
from TestSuite.MainActivity.Case002chat import Case002
from Common.RedisModule import Redis


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Case001('test'))
    suite.addTest(Case002('test'))
    Redis().set("case_num", len(suite._tests))
    runner = unittest.TextTestRunner(resultclass=result)
    rt = runner.run(suite)
    pass


