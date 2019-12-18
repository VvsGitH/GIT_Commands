# Initializing repository
print('git init')
print("git config --global user.name 'Vito Paparella S' ")
print("git config --global user.email 'vs.paparella@gmail.com' ")

# Managing files
print(''''git touch
    creates a new file''')
print('''git touch .gitignore
    creates the .gitignore file: this file contains the name of the files ignored by git''')
print('''git add .
    adds all not ignored files in the folder to the source control
    must be used every time a file is updated''')
print('''git rm --cached [file name]
    remove a file''')
print('''git status
    shows the status of the files''')
print('''git commit -m 'comment'
      marks all the added files and changes''')

# Branches
print('''git branch -a
    shows all branches''')
print('''git branch newBranch
    create a new branch''')
print('''git branch newBranch
    create a new branch''')
print('''git checkout newBranch
    moves the source control on the newBranch''')

# Push to gitHub
# Create a new empty repository on gitHub and copy the link
print('''git remote add origin https://github.com/VvsGitH/LearningGit.git
    associates the folder with a pre-create empty repository on gitHub''')
print('''git push -u origin master
    load the master branch into gitHub
    after the command push alone is enough''')
print('''git checkout featureA
    git push -u origin featureA
    load the feature branch into gitHub
    after the command push alone is enough''')
print('''git pull
    download the updates from gitHub into local''')

# Change Repository Name
# NB: Local folder name doesn't influence git synchronization
# Rename repository on gitHub, then copy the new link
print('''git remote set-url origin "new_url"
    associates the folder with the renamed repository on gitHub''')
