from datetime import datetime, time
from pytz import timezone
import requests
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Получить список сов девмана.')

    parser.add_argument(
        '--pages_count',
        '-p',
        type=int,
        default=10,
        help='Количество страниц'
    )

    args = parser.parse_args()

    if args.pages_count <= 0:
        parser.error("Количество страниц должно быть выше 0")

    return args


def load_attempts(pages_count):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    for page in range(1, (pages_count + 1)):
        users = requests.get(url, {"page": page}).json()['records']
        for user in users:
            yield user


def get_midnighters(pages_count):
    midnighters = set()
    for user in load_attempts(pages_count):
        time_ = datetime.fromtimestamp(
            user['timestamp'],
            timezone(user['timezone'])
        )
        if time(0, 0) < time_.time() < time(6, 0):
            midnighters.add(user['username'])

    return midnighters


def print_midnighters(midnighters):
    print("Полуночники девмана:")
    for username in midnighters:
        print(username)


if __name__ == '__main__':
    args = parse_args()
    midnighters = get_midnighters(args.pages_count)
    print_midnighters(midnighters)
