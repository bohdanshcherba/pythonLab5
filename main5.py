def main():
    file = b"access_log_Jul95"
    date_start = b"[01/Jul/1995:03:35"
    date_end = b"[01/Jul/1995:03:55"
    need_lines = []
    time = False

    with open(file, 'rb') as f:
        lines = f.readlines()

    for l in lines:
        if date_start in l:
            time = True
        if time:
            need_lines.append(l)
        if date_end in l:
            time = False
            break

    for l in need_lines:
        if b" 404 " in l:
            print(l.decode())

    f.close()


if __name__ == '__main__':
    main()
