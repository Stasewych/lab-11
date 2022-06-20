import re
from datetime import datetime
import zipfile


def main():
    zip_ref = zipfile.ZipFile("access_log_Jul95.zip")
    zip_ref.extractall()
    zip_ref.close()
    file_to_read = open("access_log_Jul95")
    lines = file_to_read.readlines()

    pattern = r'(\S+)\s+[-]+\s+[-]+\s+[\[](\S+)\s(\S+)]\s["](\S+)\s(\S+)\s+(\S+)["]\s([^2]\d+)\s(\d+)'
    # groups:
    # 1 - machine
    # 2 - time
    # 3 - time zone?
    # 4 - GET/POST/PUT/DELETE
    # 5 - request
    # 6 - HTTP
    # 7 - status
    # 8 - ???

    date_start = datetime.strptime('01/Jul/1995:03:35:00', '%d/%b/%Y:%H:%M:%S')
    date_end = datetime.strptime('01/Jul/1995:03:55:00', '%d/%b/%Y:%H:%M:%S')
    unique_set = set()

    for line in lines:
        x = re.match(pattern, line)
        if x:
            if date_start < datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') < date_end:
                unique_set.add(x)
            elif datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') > date_end:
                break
    for i in unique_set:
        print(i.group(1)+" " + i.group(5)+" "*5 + "Status ->" + " " + i.group(7))


if __name__ == "__main__":
    main()