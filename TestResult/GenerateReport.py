__author__ = 'Woody'

from datetime import datetime
from jinja2.environment import Template


def generate(result, startTime):
    test_cases_list = []
    report_headers = {}
    test_cases = []
    start = startTime.strftime("%Y-%m-%d %H:%M:%S")
    duration = str(datetime.now() - startTime).split(".")[0]
    status = "成功: {} 失败: {} 出错: {} 跳过: {}".format(
        len(result.successes), len(result.failures),
        len(result.errors), len(result.skipped))
    report_headers.update(dict(start_time=start, duration=duration, status=status))
    test_cases.extend(result.errors)
    test_cases.extend(result.failures)
    test_cases.extend(result.successes)
    test_cases.extend(result.skipped)
    for case in test_cases:
        case_id = case.get("case_id")
        _case = case.get("case")
        msg = case.get("msg")
        status = case.get("type")
        case_name = _case._testMethodName
        case_des = getattr(_case, _case._testMethodName+"_des")
        test_cases_list.append((case_id, case_name, status, msg, case_des))
    test_cases_list = sorted(test_cases_list, key=lambda x: x[0])
    total_test = len(test_cases_list)
    with open("templates/report_template.html", encoding="utf-8") as f:
        html = Template(f.read())
        return html.render(title="易途8安卓自动化测试报告", headers=report_headers,
                           test_cases_list=test_cases_list,total_test=total_test)