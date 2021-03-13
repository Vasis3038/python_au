import requests
import json

TOKEN = '7c3965ade72b407dcca09ad7a6b944f563dafa51'

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
GROUPS = ['1021', '1022']
ACCOUNTS =['vasis3038']

def prepare_headers():
    return {
        'Authorization': 'token {}'.format(TOKEN),
        'Content-Type': "application/json",
        'Accept': "application/vnd.github.v3+json"
    }

def prepare_body(pull, comment):
    return {
        'body': f"{comment}",
        'path': requests.get(pull['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }

def check_prefixes(message):
    message = message.split()
    pref = message[0].split('-')
    if len(pref) != 2:
        return 'ALL WRONG'
    group = pref[1]
    pref = pref[0]
    if group in GROUPS:
        if pref in PREFIXES:
            return 'OKK'
        else:
            return 'WRONG PREFIX'
    else:
        return 'WRONG GROUP'


def get_all_user_prs(user_login, repo_name, pr_state):
    user_login = f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state={pr_state}'
    res = []
    all_prs = requests.get(user_login)
    for pr in all_prs.json():
          res.append(pr)
    return res

def get_all_commits(pr):
  res = []
  link = requests.get(pr['commits_url'])
  for commit in link.json():
    res.append(commit['commit'])
  return res


def send_pr_comment(pull, comment):
    url = pull['url'] + '/comments'
    print(url)
    r = requests.post(url, headers=prepare_headers(), data=json.dumps(prepare_body(pull, comment)))
    return pull['html_url']

def verify_pr(pr):
    commits = get_all_commits(pr)
    comments = []
    if len(check_prefixes(pr['title'])) > 3:
        comment = check_prefixes(pr['title']) + ' IN PR TITLE'
        comments.append(comment)
    for commit in commits:
        if len(check_prefixes(commit['message'])) > 3:
            comment = check_prefixes(commit['message']) + ' IN COMMIT MESSAGE'
            comments.append(comment)
    if len(comments) != 0:
        send_pr_comment(pr, '\n\n'.join(comments))

if __name__ == '__main__':
    repo_name = 'python_au'
    pr_state = 'open'
    for acc in ACCOUNTS:
        all_prs = get_all_user_prs(acc, repo_name, pr_state)
        for pr in all_prs:
            verify_pr(pr)
