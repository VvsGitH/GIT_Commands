# **GIT COMMANDS LIST**
List of all the main git commands

## **Global Settings**
- git config --global user.name 'your name'
- git config --global user.email 'mail@mail'

## **Initializing repository**
- git init
- echo '# Project Name' >> README.md
  
## **Version Control**
- git status -> show which files are created/changed/deleted/renamed from the previous commit
- git log -> show the history of the comits
- git log --oneline --graph -> prettier log
- git diff -> show the differences in all files in the working area since the last commit
- git diff --staged -> show the differences in all files in the staging area since the last commit
### Commit Procedure
- git add *file_path* -> add file_name to the list of the files to commit (staging area)
- git add . -> add all folder files to the stagig area
- git commit -m 'comment' -> save the version of all the files in the stagin area
- git commit --amend -> modify the last commit: use to add/remove changes or to change the commit message 
### Discard changes in the working area
- git restore *file_path* -> remove all the changes in the file done since the last commit (NEW WAY)
- git restore . -> remove all the changes in all the files done since the last commit (NEW WAY)
- git checkout *file_path* -> remove all the changes in the file done since the last commit (OLD WAY)
- git checkout . -> remove all the changes in all the files done since the last commit (OLD WAY)
### Removing files from staging area
- git restore --staged *file_path* -> remove the file from the staging area (NEW WAY)
- git restore --staged . -> remove all files from the staging area (NEW WAY)
- git reset *file_path* -> remove the file from the staging area (OLD WAY)
- git reset -> remove all files from the staging area (OLD WAY)
### Restoring all branch to a particular commit
- git reset --soft *commit-hash* -> move the HEAD to the specified commit; all changed are kept untouched in the staging area
- git reset --mixed *commit_hash* -> move the HEAD to the specified commit; all changed are kept untouched in the working area
- git reset --hard *commit_hash* -> move the HEAD to the specified commit and remove all changes from the files
### Restoring one file to a particular commit
- git restore --source *commit_hash* *file_path* -> put the old version of the file in the working area
- git reset *commit_hash* *file_path* -> put the old version of the file in the staging area and the current version in the working area.
### Revert the repo back to the state it was previous to a particular commit
- git revert *commit_hash* -> make a new commit which put the repo in the state it was previous to the selected commit

## **Branches**
- git branch -a -> shows all branches
- git checkout *branch_name* -> moves the source control on *branch_name*
### Creating a new branch
- git branch *newBranch* -> create a new branch called *newBranch*
- git checkout -b *newBranch* -> create *newBranch* and moves the source control on it
### Merging procedure
1. git checkout *branchToUpdate* -> move the source control on the brach to update
2. git merge *branchToMerge* -> update branchToUpdate with branchToMerge
### Deleting a branch
- git branch -d *branch_name* -> delete local *branch_name* only if it was previously merged to master
- git branch -D *branch_name* -> delete local *branch_name* even if it wasn't merged to master

## **STASH**
- git stash save *stash_name* -> take the uncommitted changes and put them apart in a stash 
- git stash list -> show the list of your stashes
- git stash apply *stash_name* -> bring back to the workspace the changes in a particular stash
- git stash pop -> bring back to the workspace the changes in the last stash

## **REMOTES**
- git remote -v -> shows remote servers
- git remote show *remote_name* -> gives details about the remote
### Adding, renaming and removing a remote
- git remote add *remote_name* *remote_link*
- git remote rename *old_name* *new_name*
- gir remote remove *remote_name*
### Push/Pull
- git fetch *remote_name* -> retrieve the latest metadata from the remote
- git pull *remote_name* -> pull changes from the remote
- git push *remote_name* *branch_name* -> push your branch to the remote
- git push origin -d *branch_name* -> delete the branch on the remote

## **GitHUB**
### Load a new local repository on gitHub
1. Create a new empty repository on gitHub and copy the link
2. git remote add origin *repository_link* -> associates the folder with the empty repository
3. git push -u origin master -> load the master branch into gitHub (only the 1st time)
4. git push -u origin *feature_branch* -> load the feature branch into gitHub (only the 1st time)
### Clone a cloud repository on local
- git clone *repository_link*
### Rename repository on gitHub
- git remote set-url origin *new_url* -> associates the folder with the renamed repository on gitHub
