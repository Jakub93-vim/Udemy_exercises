import zipfile, os, re

zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_obj.extractall('extracted')

print('Current directory', os.getcwd())
print('List of subdirectories', os.listdir())

os.chdir("C:\\Users\\jakub\\Documents\\GitHub\\Udemy_exercises\\Advanced_modules\\extracted")



print('New changed directory', os.getcwd())

print('\n')

for folder, sub_folders, files in os.walk(os.getcwd()):

    for file in files:
        f = open(os.path.join(folder,file), 'r')
        content= f.read()

        if re.findall('\d\d\d-\d\d\d-\d\d\d\d',content):
            number = re.findall('\d\d\d-\d\d\d-\d\d\d\d',content)
            print(f'Number is in {file} and it is {number}')