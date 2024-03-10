import time
import git  # pip install gitpython
from git import RemoteProgress
import json

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message) 

getgit(gitlink, branch, dir):
    print('Cloning into %s' % git_root)
    git.Repo.clone_from(gitlink, dir, 
            branch=branch, progress=CloneProgress())

class AutoRedeploy():
    def run():
        while auto:
            with open('strings.json') as f:
                data = json.load(f)
                    for x in data[]:
                        name=x
                        link=x[0]
                        branch=x[1]
                        rcom=x[2]

                        curver = open(name+"/version.txt"
                
                        repo = git.repo(link, branch)
                        sha = repo.head.object.hexsha
                        if sha != curver:
                            getgit()
    """ TODO
        - Define curver and auto
        - auto branch and dir
        - catch/disable
    """
