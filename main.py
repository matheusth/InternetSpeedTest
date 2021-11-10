from internet_test import perform_tests
from report import Report
import json
import sys


def parse_config_file():
    with open('config.json', 'r') as config_file:
        print(json.load(config_file))


def main():
    pass


if __name__ == '__main__':
    parse_config_file()
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
