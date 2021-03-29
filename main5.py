import re

def main():
    start_date = r"([a-zA-Z0-9._-]+)( - - )(\[01/Jul/1995:)(03:3[5-9]:[0-9]|03:55:00)([a-zA-Z0-9. _/-]+)]" \
                 r"(.+) [4-5]{1}[0-9]{1}[0-9]{1} (.+)"
    after_date = r"([a-zA-Z0-9._-]+)( - - )(\[01/Jul/1995:)(03:[4-5][0-9]:\d{2}|03:35:00)([a-zA-Z0-9. _/-]+)]" \
                 r"(.+) [4-5]{1}[0-9]{1}[0-9]{1} (.+)"
    stop_date = r"([a-zA-Z0-9._-]+)( - - )(\[01/Jul/1995:)(03:55:00|03:55:00)([a-zA-Z0-9. _/-]+)]" \
                r"(.+) [4-5]{1}[0-9]{1}[0-9]{1} (.+)"

    date1 = re.compile(start_date)
    date2 = re.compile(stop_date)
    date3 = re.compile(after_date)

    with open('access_log_Jul95', 'r') as file:
        found = []
        for line in file:
            match = date1.search(line)
            after_date = date3.search(line)
            stop_match = date2.search(line)
            if match:
                found.append(match)
            elif after_date:
                found.append(after_date)
            if stop_match:
                break

        for line in found:
            print(line.group())


if __name__ == '__main__':
    main()
