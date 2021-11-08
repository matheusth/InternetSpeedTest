import socket

from speedtest import Speedtest
from datetime import datetime
from report import Report
import sys
import _thread


def choose_best_server(test: Speedtest) -> Speedtest:
    print("Getting server list...")
    test.get_servers()
    print("Chosing best server...")
    best_server = test.get_best_server()
    print(f"Found: {best_server['host']}, location: {best_server['country']}")
    return test


def perform_test(test: Speedtest):
    moment = datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    download_result = test.download()
    upload_result = test.upload()
    download_result_mbits = download_result / 1048576
    upload_result_mbits = upload_result / 1048576

    return {'moment': moment, 'upload': f'{upload_result_mbits:.3f}', 'download': f'{download_result_mbits:.3f}'}


def get_keys(a_list: list):
    input()
    a_list.append(True)


def perform_tests(source: str):
    test = Speedtest(source_address=source)
    test = choose_best_server(test)

    a_list = []
    _thread.start_new_thread(get_keys, (a_list,))
    while not a_list:
        yield perform_test(test)


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
