import os
import git
path = "."
files= os.listdir(path)
s = []
for file in files:
  try:
     if os.path.isdir(file):
          #g = git.cmd.Git(path+"/"+file)
          repo = git.Repo(path+"/"+file)
#          for item in repo.index.diff(None):
#               print(item.a_path)
          print(repo)
          repo.git.stash('save')
          repo.git.checkout('master')
          repo.remotes.origin.fetch()
          repo.git.reset('--hard','origin/master')          
#g.pull()

  except Exception:
     pass
