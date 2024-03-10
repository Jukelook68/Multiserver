import time
import git  # pip install gitpython
from git import RemoteProgress
import json

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message) 

getgit(gitlink, branch, name):
    print('Cloning into %s' % git_root)
    repo = git.Repo.clone_from(gitlink, "projects/"+name, 
            branch=branch, progress=CloneProgress())
    f = open("projects/"+name+"/multiserver.txt", "x")
    f.write(str(repo.head.object.hexsha))
    f.close()

class AutoRedeploy():
    def run(time):
        while auto:
            with open('config.json') as f:
                data = json.load(f)
                    for x in data[]:
                        name=x
                        link=x[0]
                        branch=x[1]
                        rcom=x[2]

                        curver = open("projects/"+name+"/multiserver.txt")
                
                        repo = git.repo(link, branch)
                        sha = str(repo.head.object.hexsha)
                        if sha != curver:
                            getgit(link, branch, name)
        sleep(time)
    """ TODO
        - Define curver and auto
        - auto branch and dir
        - catch/disable
    """
