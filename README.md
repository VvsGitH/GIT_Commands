# **GIT COMMANDS LIST**
List of all the main git commands

## **Global Settings**
- git config --global user.name 'your name'
- git config --global user.email 'mail@mail'

## **Initializing repository**
- git init
- echo '# Project Name' >> README.md

## **Managing files**
- touch *new_file*
- touch .gitignore -> this file contains the name of the files ignored by git'''
- mkdir *new_dir*
  
## **Commit procedure**
1. git status -> show which files are created/changed/deleted/renamed from the previous commit
2. git add *file_name* -> add file_name to the list of the files to commit
2. git add . -> add all folder files to the list of to commit files
2. git rm --cached *file_name* -> remove file from the list
2. git rm -r --cached . -> remove all folder files from the list
3. git commit -m 'comment'
### Resetting
- git reset --hard -> reset the folder to the last commit

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

## **GitHUB**
### Load a new local repository on gitHub
1. Create a new empty repository on gitHub and copy the link
2. git remote add origin *repository_link* -> associates the folder with the empty repository
3. git push -u origin master -> load the master branch into gitHub (only the 1st time)
4. git push -u origin *feature_branch* -> load the feature branch into gitHub (only the 1st time)
### Clone a cloud repository on local
- git clone *repository_link*
### Push/Pull
- git pull -> pull from gitHub
- git push -> push your current branch to gitHub
- git push origin -d *branch_name* -> delete the *branch_name* on gitHub

## **Change repository name**
### Change local repository name
- Local folder name doesn't influence git synchronization
### Rename repository on gitHub, then copy the new link
- git remote set-url origin *new_url* -> associates the folder with the renamed repository on gitHub
