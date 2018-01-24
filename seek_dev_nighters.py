from datetime import datetime, time
from pprint import pprint

from collections import defaultdict
from pytz import timezone

import requests


def load_attempts(pages_count=10):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    for page in range(1, (pages_count + 1)):
        users = requests.get(url, {"page": page}).json()['records']
        for user in users:
            yield user


def get_midnighters():
    midnighters = set()
    for user in load_attempts():
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
    midnighters = get_midnighters()
    print_midnighters(midnighters)
