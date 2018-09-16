'''
import os
# pick a folder you have ...
folder = 'C:/'
folder_size = 0
for (path, dirs, files) in os.walk(folder):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
print ("Folder = %0.1f MB" % (folder_size/(1024*1024.0)))'''

'''
import os
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += (os.path.getsize(fp) if os.path.isfile(fp) else 0)
    return total_size

print (get_size())
'''

def getDirectorySize(directory):
    
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    return dir_size
