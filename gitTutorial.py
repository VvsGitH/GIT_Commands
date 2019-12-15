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
print('''git remote add origin https://github.com/VvsGitH/LearningGit.git
    shows all branches''')
print('''git git push -u origin master
    load on gitHub''')
