'''
Created on May 3, 2019

@author: phil
'''
import os
import fnmatch
import zipfile
from zipfile import ZipFile 
from datetime import datetime,timedelta


# detect the current working directory
path = os.chdir("d:\Test")
path2 = 'd:\Test_zip'

today=datetime.now()
yesterday = (datetime.now() - timedelta(1)).strftime('%m-%d-%Y')
#today = date.strftime("%m-%d-%Y")
#date = now.strftime("%m-%d-%Y")
print("today=", today.strftime("%m-%d-%Y"))
print("yesterday=", yesterday)
date = today.strftime("%m-%d-%Y")
print(date)

#date = datetime.date.today()
#date_time = today.strftime("%m-%d-%Y")
print("date:",date)
pattern = f'*{yesterday}*'

print('Pattern :', pattern)
print(date)
# read the entries
with os.scandir(path) as listOfEntries: 

    for entry in listOfEntries:
        base = os.path.splitext(os.path.basename(entry))[0]
        print('file base name', base) 
        print('filepath=', path)
        # print all entries that are files
        if entry.is_file():
            #print(entry.name)
            if fnmatch.fnmatch(entry, pattern):
                print('Matching entry name = ',entry.name)
                
                print('Present Dir =', path2)
                #ZipFile(f'{entry}.zip', 'w').write(entry.name):
                with ZipFile(f'{path2}\{base}.zip','w') as zipfile: 
             
                        print ("zipfile =", entry)
                        zipfile.write(entry) 
                            #ZipFile.close(zipfile)