from datetime import datetime
from pytz import timezone
import requests


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    page_number = 1
    while True:
        page = requests.get(url, {'page': page_number}).json()
        attempts = page['records']
        for attempt in attempts:
            yield attempt
        if page_number >= page['number_of_pages']:
            break
        page_number += 1


def get_midnighters(attempts_generator):
    midnighters = set()
    for attempt in attempts_generator:
        attempt_time = datetime.fromtimestamp(
            attempt['timestamp'],
            timezone(attempt['timezone'])
        )
        if 0 < attempt_time.hour < 6:
            midnighters.add(attempt['username'])

    return midnighters


def print_midnighters(midnighters):
    print('Полуночники девмана:')
    for username in midnighters:
        print(username)


if __name__ == '__main__':
    attempts_generator = load_attempts()
    midnighters = get_midnighters(attempts_generator)
    print_midnighters(midnighters)
