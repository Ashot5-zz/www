def main(mtime: str) -> str:
    hour, minute = map(lambda x: x[1] - int(x[0]), zip(mtime.split(':'), (23, 60)))

    if hour > 12:
        hour -= 12
    if minute == 60:
        minute = 0
        hour += 1

    return '{:02d}:{:02d}'.format(hour, minute)


def what_is_the_time(time_in_mirror):
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)


if __name__ == '__main__':
    print('12:22 -->', main('12:22'))
    print('05:25 -->', main('05:25'))
    print('01:50 -->', main('01:50'))
    print('11:58 -->', main('11:58'))
    print('12:01 -->', main('12:01'))
    print('09:00 -->', main('09:00'))
    print('06:00 -->', main('06:00'))
    print('12:00 -->', main('12:00'))
    print('01:00 -->', main('01:00'))
