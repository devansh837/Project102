import os
import shutil
from_dir=""
to_dir=""
listoffiles=os.listdir(from_dir)
print(listoffiles)
for fname in listoffiles:
    name,extension=os.path.splitext(fname)
    print(name)
    print(extension)
if extension == '':
   continue
if extension in['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+fname
        path2=to_dir+'/'+""
        path3=to_dir+'/'+""+"/"+fname
        print("path1",path1)
        print("path3",path3)
        
if os.path.exists(path2):
  print("moving" + fname + "")

  shutil.move(path1,path3)

  else:
    os.makedirs(path2)
    print("moving" + fname + "")
    shutil.move(path1,path3)        
