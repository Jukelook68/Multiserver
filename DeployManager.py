import time
import git  # pip install gitpython
from git import RemoteProgress

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)
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
