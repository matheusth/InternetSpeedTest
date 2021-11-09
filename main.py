from internet_test import perform_tests
from report import Report
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SOURCE_IP = sys.argv[1]
    else:
        raise Exception("Error no source ip provided!")

    report = Report()
    row = 1
    for result_dict in perform_tests(SOURCE_IP):
        row += 1
        report.write_file(result_dict)
        print(result_dict)
