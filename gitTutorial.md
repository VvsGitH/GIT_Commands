# PYTHON COMMANDS LIST

## Global Settings
- git config --global user.name 'Vito Paparella S.'
- git config --global user.email 'vs.paparella@gmail.com'

## Initializing repository
- git init
- echo "# Project Name' >> README.md

## Managing files
- touch new_file
- mkdir new_dir
- touch .gitignore -> this file contains the name of the files ignored by git'''
  
## Commit procedure
- git status -> show which files are created/changed/deleted/renamed from the previous commit
- git add file_name -> add file_name to the list of the files to commit
- git add . -> add all folder files to the list of to commit files
- git rm --cached file_name -> remove file from the list
- git commit -m 'comment'

## Resetting
- git reset --hard -> reset the folder to the last commit

## Branches
- git branch -a -> shows all branches
- git branch newBranch -> create a new branch called newBranch
- git checkout newBranch -> moves the source control on the newBranch
- git checkout -b newBranch -> create newBranch and moves the source control on it

## Merging procedure
- git checkout branchToUpdate -> move the source control on the brach to update
- git merge branchToMerge -> update branchToUpdate with branchToMerge

## Configure new gitHub repository
- Create a new empty repository on gitHub and copy the link
- git remote add origin repository_link -> associates the folder with the empty repository
- git push -u origin master -> load the master branch into gitHub (only the 1st time)

## GitHub push/pull
- git push -> push to gitHub
- git pull -> pull from gitHub
- git push -u origin featureA -> load the feature branch into gitHub (only the 1st time)

## Change Repository Name
- Local folder name doesn't influence git synchronization

## Rename repository on gitHub, then copy the new link
- git remote set-url origin "new_url" -> associates the folder with the renamed repository on gitHub
