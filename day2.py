import util

def _parse_report(report):
    return [int(n) for n in filter(None, report.split(' '))]


def _is_safe(report):
    is_increasing = report[0] < report[1]
    if is_increasing:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff <= 0 or diff > 3:
                return False
    else:
        for i in range(1, len(report)):
            diff = report[i-1] - report[i]
            if diff <= 0 or diff > 3:
                return False
    return True


def count_safe_reports(filename):
    reports = util.read_lines_from_file(filename)
    parsed_reports = [_parse_report(report) for report in reports]
    safety_reports = [_is_safe(report) for report in parsed_reports]
    return safety_reports.count(True)


def _is_safe_with_dampener(report):
    if _is_safe(report):
        return True
    for i in range(len(report)):
        sliced_report = report[:i] + report[i+1:]
        if _is_safe(sliced_report):
            return True
    return False


def count_safe_reports_with_dampener(filename):
    reports = util.read_lines_from_file(filename)
    parsed_reports = [_parse_report(report) for report in reports]
    safety_reports = [_is_safe_with_dampener(report) for report in parsed_reports]
    return safety_reports.count(True)
            
