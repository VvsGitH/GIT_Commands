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
- git diff -> show the differences in all modified files in respect to the last commit
### Commit Procedure
- git add *file_path* -> add file_name to the list of the files to commit (staging area)
- git add . -> add all folder files to the stagig area
- git commit -m 'comment' -> save the version of all the files in the stagin area
- git commit -a -m 'comment' -> add all files to the staging area and save their version
- git commit --amend -> modify the last commit: use to add/remove changes or to change the commit message 
### Removing files from staging area
- git restore --staged *file_path* -> remove the file from the staging area
- git reset *file_path* -> remove the file from the staging area
- git restore --staged . -> remove all files from the staging area
- git reset -> remove all files from the staging area
### Restoring to the last commit
- git restore *file_path* -> bring the file version to the last commit
- git restore . -> restore all folder to the last commit
- git checkout -- *file_path*
- git reset --hard -> reset all files to the last commit
### Restoring to a particular commit
- git checkout *commit_hash* -- *file_path*
- git reset --hard *commit_hash* -> reset the entire repository

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
