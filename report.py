import csv
from os import path, curdir
from datetime import date
from datetime import datetime


class Report:
    def __init__(self, filepath: str = None, source_ip: str = "no-source-ip"):
        self.filepath = path.join(curdir,
                                  f'{source_ip}'
                                  '-{str(date.today().strftime("%B"))}.csv')

    def write_file(self, info: dict):
        is_file_new = not path.exists(self.filepath)
        with open(self.filepath, 'a') as csv_file:
            fieldnames = ['moment', 'source_ip', 'upload', 'download']
            report_writer = csv.DictWriter(csv_file, fieldnames)
            if is_file_new:
                report_writer.writeheader()

            report_writer.writerow(info)
