import requests
import json

TOKEN = f'99c16269c55c64669c0f6ec5a77bd4be0c0'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": TOKEN,
    }

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'VERIFIER']
GROUPS = ['1021', '1022']

def read_file():
    f = open('links.txt', 'r')
    file = f.readlines()
    f.close()
    return file

def check_title(pr):
    title = pr['title'].split()
    pref = title[0].split('-')
    if len(pref) != 2:
        return False
    group = pref[1]
    pref = pref[0]
    if group in GROUPS and pref in PREFIXES:
        return True
    else:
        return False

def print_pr(file):
    for lines in file:
        line = lines[:-1]
        name = line[29:-16]
        print(name)
        all_prs = requests.get(line)
        print(all_prs)
        for pr in all_prs.json():
            print('state is', pr['state'])
            print(pr['title'])

def print_wrong_titles(file):
    for lines in file:
        line = lines[:-1]
        name = line[29:-16]
        print(name)
        all_prs = requests.get(line)
        print(all_prs)
        print('Wrong titles:')
        for pr in all_prs.json():
            if (check_title(pr) is False):
                print(pr['title'])

def print_commits(file):
    for lines in file:
        line = lines[:-1]
        name = line[29:-16]
        print(name)
        all_prs = requests.get(line)
        print(all_prs)
        for pr in all_prs.json():
            print(pr['commits_url'])
            message = requests.get(pr['commits_url'])
            for commit in message.json():
                print(commit['commit']['message'])

if __name__ == '__main__':
    file = read_file()
    print_commits(file)
