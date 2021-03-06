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

def get_all_user_pr(user_login, repo_name, pr_state):
    user_login = 'https://api.github.com/repos/' + user_login
    user_login = user_login + '/' + repo_name + '/pulls'
    res = []
    all_prs = requests.get(user_login)
    for pr in all_prs.json():
        if(pr['state'] == pr_state):
          res.append(pr)
    return res

def get_all_commits(pr):
  print(pr['commits_url'])
  res = []
  message = requests.get(pr['commits_url'])
  for commit in message.json():
    res.append(commit['commit'])
  return res



if __name__ == '__main__':
    file = read_file()
    print_commits(file)
