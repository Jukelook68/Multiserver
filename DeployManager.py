import time
import git  # pip install gitpython
from git import RemoteProgress
import json

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)

getconfig()
    with open('strings.json') as f:
        data = json.load(f)
        for x in data[]:
            name=x
            link=x[0]
            rcom=x[1]
            branch[2]

getgit(gitlink, branch, dir):
    print('Cloning into %s' % git_root)
    git.Repo.clone_from(gitlink, dir, 
            branch=branch, progress=CloneProgress())

class AutoRedeploy(links):
    run():
        while auto:
            for x in len(links):
                repo = git.repo(links[x])
                sha = repo.head.object.hexsha
                if sha != curver:
                    getgit(link[x])
    """ TODO
        - Define curver and auto
        - auto branch and dir
        - catch/disable
    """
