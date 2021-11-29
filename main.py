import schedule

from internet_test import perform_tests
from report import Report
from time import sleep
import _thread as thread
import json


def parse_config_file():
    with open('config.json', 'r') as config_file:
        config_dict = json.load(config_file)
    return config_dict


def open_test_thread(source_ip):
    test_thread = thread.start_new_thread(perform_test_job, source_ip)


def perform_test_job(source_ip):
    report = Report()
    test_result = next(perform_tests(source_ip))
    print(test_result)
    report.write_file(test_result)


def schedule_tests(test_at, source_ip):
    schedule.every().day.at(test_at).do(perform_test_job, open_test_thread, source_ip)


def main():
    parsed_config = parse_config_file()
    try:
        source_ip = parsed_config['source_ip']
        test_at = parsed_config['test_at']
        number_of_tests = parsed_config['number_of_tests']

        schedule_tests(test_at, source_ip)

    except KeyError:
        print('No source ip provided in the config file')
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
