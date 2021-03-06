import requests
import json

TOKEN = f'd89f3c9bb2c3cf2e4f7a7b16e5811a00716ebbfb'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": TOKEN,
    }

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
GROUPS = ['1021', '1022']

def check_prefixes(title):
    title = title.split()
    pref = title[0].split('-')
    if len(pref) != 2:
        return False
    group = pref[1]
    pref = pref[0]
    if group in GROUPS:
        if pref in PREFIXES:
            return 'OKK'
        else:
            return 'WRONG PREFIX'
    else:
        return 'WRONG GROUP'

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
  #print(pr['commits_url'])
  res = []
  link = requests.get(pr['commits_url'])
  for commit in link.json():
    res.append(commit['commit'])
  return res

#def send_pr_comment(pr, errors):




if __name__ == '__main__':
    f = 'alexarlord-boop'
    repo_name = 'python_au'
    pr_state = 'open'
    print(get_all_user_pr(f, repo_name, pr_state))
