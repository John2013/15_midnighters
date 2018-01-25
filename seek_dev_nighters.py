from datetime import datetime
from pytz import timezone
import requests


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    page1 = requests.get(url, {'page': 1}).json()
    pages_count = page1['number_of_pages']
    for page_number in range(1, (pages_count + 1)):
        if page_number == 1:
            attempts = page1['records']
        else:
            attempts = requests.get(url, {'page': page_number}).json()[
                'records'
            ]

        for attempt in attempts:
            yield attempt


def get_midnighters():
    midnighters = set()
    for attempt in load_attempts():
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
    midnighters = get_midnighters()
    print_midnighters(midnighters)
