from speedtest import Speedtest
from datetime import datetime
from report import Report
import sys
import threading


def choose_best_server(test: Speedtest) -> Speedtest:
    print("Getting server list...")
    test.get_servers()
    print("Chosing best server...")
    best_server = test.get_best_server()
    print(f"Found: {best_server['host']}, location: {best_server['country']}")
    return test


def perform_test(test: Speedtest):
    print("was called")
    moment = datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    download_result = test.download()
    upload_result = test.upload()
    download_result_mbits = download_result / 1000000
    upload_result_mbits = upload_result / 1000000

    return {
            'moment': moment,
            'source_ip': test._source_address,
            'upload': f'{upload_result_mbits:.3f}',
            'download': f'{download_result_mbits:.3f}'
           }


def get_keys(a_list: list):
    input()
    a_list.append(True)


def perform_tests(source: str):
    print("was called")
    test = Speedtest(source_address=source)
    test = choose_best_server(test)
    a_list = []
    input_threading = threading.Thread(target=get_keys, args=(a_list,))
    input_threading.start()

    while not a_list:
        yield perform_test(test)


def setup():
    if len(sys.argv) > 1:
        source_ips = sys.argv[1:]
        for source_ip in source_ips:
            testing = threading.Thread(target=invoke_testing,
                                       args=(source_ip,))
            testing.start()
            print("started...")
        print(sys.argv)
    else:
        raise Exception("Error no source ip provided!")


def invoke_testing(source_ip: str):
    print("was called")
    report = Report(source_ip=source_ip)
    row = 1
    for result_dict in perform_tests(source_ip):
        row += 1
        report.write_file(result_dict)
        print(result_dict)


setup()
