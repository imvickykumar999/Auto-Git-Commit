
# https://github.com/imvickykumar999/100th-Repository-Morsetor-python-Package/blob/main/PYPI%20python%20package/multivicks/github.py
# https://github.com/imvickykumar999/Auto-Git-Commit/blob/master/streaks_.py

import os

def upload():
    print('\n1). git init')
    os.system('git init')

    print('\n2). git add .')
    os.system('git add .')

    # file = input('\nEnter each file name seperated by space (or, Press ENTER to Upload All...) : ')
    file = ''
    print('\n3). git commit -m "Adding files"')
    os.system('git commit '+ file +' -m "Adding files"')

    print('\n4). git remote add origin https://github.com/...')
    # username = input("Enter the github Username : ")
    username = 'imvickykumar999'

    # reponame = input('Enter Existing Repository : ')
    reponame = 'Auto-Git-Commit'
    os.system('git remote add origin https://github.com/'+username+'/'+reponame+'.git')

    print('\n5). git pull origin master')
    os.system('git pull origin master')

    print('\n6). git push origin master')
    return_force = os.system('git push --force origin master')

    if not return_force:
        print('Uploaded Successfully')
    else:
        print("Sorry, Couldn't be uploaded... Try again !!!")

upload()