from datetime import datetime
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
        parser.error(
            'Количество страниц должно быть выше 0, задано: {}'.format(
                args.pages_count
            )
        )

    return args


def load_attempts(pages_count):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    for page in range(1, (pages_count + 1)):
        attempts = requests.get(url, {'page': page}).json()['records']
        for attempt in attempts:
            yield attempt


def get_midnighters(pages_count):
    midnighters = set()
    for user in load_attempts(pages_count):
        attempt_time = datetime.fromtimestamp(
            user['timestamp'],
            timezone(user['timezone'])
        )
        if 0 < attempt_time.hour < 6:
            midnighters.add(user['username'])

    return midnighters


def print_midnighters(midnighters):
    print('Полуночники девмана:')
    for username in midnighters:
        print(username)


if __name__ == '__main__':
    args = parse_args()
    midnighters = get_midnighters(args.pages_count)
    print_midnighters(midnighters)
