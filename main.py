from internet_test import perform_tests
from report import Report
import json


def parse_config_file():
    with open('config.json', 'r') as config_file:
        config_dict = json.load(config_file)
    return config_dict


def main():
    parsed_config = parse_config_file()

    try:
        source_ip = parsed_config['source-ip']
        report = Report()

        row = 1
        for result_dict in perform_tests(source_ip):
            row += 1
            report.write_file(result_dict)
            print(result_dict)

    except KeyError:
        print('No source ip configured provided in the config file')


if __name__ == '__main__':
    main()
