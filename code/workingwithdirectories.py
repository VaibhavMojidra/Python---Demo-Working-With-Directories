#Working with directories

import os

#Returns Current Directory

print(os.getcwd())


#Create directory

os.mkdir('Vaibhav')

#Change Directory

os.chdir('Vaibhav')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('Sample')

#Able To delete directory without files

os.rmdir('DirectoryWithoutFiles')

#Check files in folder

print(os.listdir('DirectoryWithFiles'))


#Print with join as join in linux based is '/'  and windows is '\'

print(os.path.join('Vaibhav','Mojidra'))

#Unable To delete directory without files

os.rmdir('DirectoryWithFiles')

