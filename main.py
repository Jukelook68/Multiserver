from Threading import Thread
import git
import DeployManager

with open('config.json') as f:
        data = json.load(f)
        for x in data[0]:
            name=x
            link=x[0]
            branch=x[1]
            rcom=x[2]
            
            gitget(link, branch, name)
            importlib.devalidatecache()
            project = importlib.import_module("programs/"+name)
            Thread(target = run).start()

        autotime=data[1][0]
        DeployManager.AutoDeploy.run()


