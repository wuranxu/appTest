__author__ = 'Woody'

import unittest

from HtmlTestRunner import HTMLTestRunner
from TestResult.Result import result
from TestSuite.MainActivity.Case001User import Case001
from TestSuite.MainActivity.Case002chat import Case002
from Common.RedisModule import Redis
from datetime import datetime
from TestResult.GenerateReport import generate


if __name__ == "__main__":
    report_headers = {}
    start = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(Case001('test'))
    suite.addTest(Case001('test_222'))
    suite.addTest(Case001('test_2321'))
    suite.addTest(Case002('test'))
    Redis().set("case_num", len(suite._tests))
    runner = unittest.TextTestRunner(resultclass=result)
    rt = runner.run(suite)
    html = generate(rt, start)
    with open("reports/report{}.html".format(datetime.strftime(datetime.now(), "%Y-%m-%d %H-%M-%S")), "w", encoding="utf-8") as f:
        f.write(html)



